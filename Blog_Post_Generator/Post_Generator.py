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
    )

    def run(self, topic: str, use_cache: bool = True):
        logger.info(f"Generating blog post for topic: {topic}")

        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                return cached_blog_post

        search_results = self._get_search_results(topic)
        if not search_results:
            return f"No search results found for topic: '{topic}'"

        return self._write_blog_post(topic, search_results)

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]) -> None:
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

    def _get_search_results(self, topic: str):
        try:
            response = self.searcher.run(topic)
            return response.content
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return None

    def _write_blog_post(self, topic: str, search_results):
        writer_input = f"Topic: {topic}\nSearch Results: {search_results}"
        
        response = self.writer.run(writer_input)
        blog_post = response.content
        self._add_blog_post_to_cache(topic, blog_post)
        return blog_post

if __name__ == "__main__":
    from rich.prompt import Prompt

    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]\n")

    generate_blog_post = BlogPostGenerator()

    response = generate_blog_post.run(topic=topic, use_cache=False)
    print("\n" + "="*80)
    print("GENERATED BLOG POST:")
    print("="*80)
    print(response)