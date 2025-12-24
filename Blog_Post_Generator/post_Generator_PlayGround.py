import json
from typing import Optional, List, Iterator
from pydantic import BaseModel, Field
from agno.workflow import Workflow, RunResponse
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger
from agno.playground import playground, serve_playground_app
from agno.storage.workflow.sqlite import SqliteWorkflowStorage


# -----------------------------
# Data Models
# -----------------------------

class NewsArticle(BaseModel):
    title: str = Field(
        description="Title of the article"
    )
    url: str = Field(
        description="URL of the article"
    )
    summary: Optional[str] = Field(
        description="Short summary of the article (if available)"
    )


class SearchResults(BaseModel):
    articles: List[NewsArticle]


# -----------------------------
# Workflow Definition
# -----------------------------

class BlogPostGenerator(Workflow):

    # Agent 1: Searches articles
    searcher = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Given a topic, search for the top 5 relevant news articles."
        ],
        add_datetime_to_instructions=True,
        response_model=SearchResults,
        structured_outputs=True,
        debug_mode=True,
        show_tool_calls=True,
    )

    # Agent 2: Writes blog post
    writer = Agent(
        model=Gemini(id="gemini-2.0-flash-thinking-exp-01-21"),
        instructions=[
            "You will receive a topic and a list of articles.",
            "Write a New York Times–style blog post.",
            "Use engaging section headings.",
            "Include key takeaways.",
            "Always cite sources."
        ],
        markdown=True,
        debug_mode=True,
    )

    # -----------------------------
    # Workflow Entry Point
    # -----------------------------

    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        logger.info(f"Generating blog post for topic: {topic}")
        logger.info(f"use_cache: {use_cache}")

        # Check cache
        if use_cache:
           cached_blog_post = self._get_cached_blog_post(topic)
           if cached_blog_post:
               logger.info(f"Using cached blog post for topic: '{topic}'")
               yield RunResponse(content=cached_blog_post,event=RunEvent.workflow_completed)
               return

        # Step 2: Search for Articles
        search_results = self._get_search_results(topic)
        if not search_results or len(search_results.articles) == 0:
            logger.warning(f"No search results found for topic: '{topic}'")
            yield RunResponse(content=f"No search results found for topic: '{topic}'",event=RunEvent.workflow_completed)
            return

        # Step 3: Write the Blog Post
        yield from self._write_blog_post(topic, search_results)

    # -----------------------------
    # Cache Helpers
    # -----------------------------

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]) -> None:
        logger.info(f"Caching blog post for topic: '{topic}'")

        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

        logger.info("Blog post cached successfully")

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        logger.info(f"Checking cache for topic: '{topic}'")

        cached_post = self.session_state.get("blog_posts", {}).get(topic)

        if cached_post:
            logger.info("Cache hit")
        else:
            logger.info("Cache miss")

        return cached_post

    # -----------------------------
    # Search Logic with Retry
    # -----------------------------

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        MAX_ATTEMPTS = 3

        for attempt in range(MAX_ATTEMPTS):
            try:
                logger.info(f"Attempt {attempt + 1}: Searching articles for '{topic}'")

                response = self.searcher.run(topic)

                if response and isinstance(response.content, SearchResults):
                    logger.info(
                        f"Found {len(response.content.articles)} articles"
                    )
                    return response.content

                logger.warning("Invalid or empty search response")

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")

        logger.error(
            f"Failed to retrieve search results after {MAX_ATTEMPTS} attempts"
        )
        return None
    def write_blog_post(self, topic: str, search_results: SearchResults) -> Iterator[RunResponse]:
        logger.info(f"Writing blog post for topic: '{topic}'")

        writer_input = {
            'topic': topic,
            'articles': [article.model_dump() for article in search_results.articles]
        }

        logger.info(f"Input prepared for writer agent: {json.dumps(writer_input, indent=4)}")

        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)

        self._add_blog_post_to_cache(topic, self.writer.run_response.content)

generate_blog_post = BlogPostGenerator(
    name='Blog Post Generator',
    # session_id=f'generate_blog_post',
    workflow_id='generate_blog_post',
    storage=SqliteWorkflowStorage(
        table_name='generate_blow_post_workflows',
        db_file='./storage/workflows.db'
    )
)

app = Playground(
    workflows=[
        generate_blog_post
    ]
).get_app()


if __name__ == "__main__":
    serve_playground_app('blog_post_generator_workflow: app', reload=True)
    # from rich.prompt import Prompt
    # from agno.storage.workflow.sqlite import SqliteWorkflowStorage
    # from agno.utils.pprint import pprint_run_response

    # # Get topic from user
    # topic = Prompt.ask(
    #     "[bold]Enter a blog post topic[/bold]\n",
    # )
    # url_safe_topic = topic.lower().replace(" ", "-")

    # generate_blog_post = BlogPostGenerator(
    #     session_id=f'generate_blog_post_{url_safe_topic}',
    #     storage=SqliteWorkflowStorage(
    #         table_name='generate_blog_post_workflows',
    #         db_file='./storage/workflows.db'
    #     )
    # )

    # response = generate_blog_post.run(topic=topic, use_cache=False)

    # pprint_run_response(response, markdown=False)


