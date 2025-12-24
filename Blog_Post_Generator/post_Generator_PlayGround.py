import json
import os
from typing import Optional, List
from pydantic import BaseModel, Field
from agno.workflow import Workflow
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from rich.prompt import Prompt
from agno.utils.pprint import pprint_run_response

# Set API keys
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

class NewsArticle(BaseModel):
    title: str = Field(description="Title of the article")
    url: str = Field(description="URL of the article")
    summary: Optional[str] = Field(description="Short summary of the article (if available)")

class SearchResults(BaseModel):
    articles: List[NewsArticle]

class BlogPostGenerator(Workflow):
    searcher = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        instructions=["Given a topic, search for the top 5 relevant news articles."],
        add_datetime_to_instructions=True,
        response_model=SearchResults,
        structured_outputs=True,
        debug_mode=True,
        show_tool_calls=True,
    )

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

    def run(self, topic: str, use_cache: bool = True):
        logger.info(f"Generating blog post for topic: {topic}")

        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                return cached_blog_post

        search_results = self._get_search_results(topic)
        if not search_results or len(search_results.articles) == 0:
            return f"No search results found for topic: '{topic}'"

        return self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]) -> None:
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str) -> Optional[SearchResults]:
        try:
            response = self.searcher.run(topic)
            if response and isinstance(response.content, SearchResults):
                return response.content
        except Exception as e:
            logger.error(f"Search failed: {e}")
        return None

    def _write_blog_post(self, topic: str, search_results: SearchResults):
        writer_input = {
            'topic': topic,
            'articles': [article.model_dump() for article in search_results.articles]
        }
        
        response = self.writer.run(json.dumps(writer_input, indent=4))
        blog_post = response.content
        self._add_blog_post_to_cache(topic, blog_post)
        return blog_post

if __name__ == "__main__":
    # Get topic from user
    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]\n")
    url_safe_topic = topic.lower().replace(" ", "-")

    generate_blog_post = BlogPostGenerator(
        session_id=f'generate_blog_post_{url_safe_topic}',
        storage=SqliteWorkflowStorage(
            table_name='generate_blog_post_workflows',
            db_file='./storage/workflows.db'
        )
    )

    response = generate_blog_post.run(topic=topic, use_cache=False)
    pprint_run_response(response, markdown=True)