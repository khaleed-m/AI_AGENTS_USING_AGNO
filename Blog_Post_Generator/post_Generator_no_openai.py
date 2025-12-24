import json
import os
from typing import Optional, List
from pydantic import BaseModel, Field
from agno.workflow import Workflow
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.log import logger

# Set API keys
os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"  # Add your Google API key

class NewsArticle(BaseModel):
    title: str = Field(description="Title of the article")
    url: str = Field(description="URL of the article")
    summary: Optional[str] = Field(description="Short summary of the article (if available)")

class SearchResults(BaseModel):
    articles: List[NewsArticle]

class BlogPostGenerator(Workflow):
    # Only use Gemini for both search and writing
    gemini_agent = Agent(
        model=Gemini(id="gemini-2.0-flash-thinking-exp-01-21"),
        tools=[DuckDuckGoTools()],
        instructions=[
            "You are a blog post generator.",
            "First, search for recent articles about the given topic using DuckDuckGo.",
            "Then write a comprehensive New York Times-style blog post.",
            "Use engaging section headings and include key takeaways.",
            "Always cite your sources."
        ],
    )

    def run(self, topic: str, use_cache: bool = True):
        logger.info(f"Generating blog post for topic: {topic}")

        if use_cache:
            cached_blog_post = self._get_cached_blog_post(topic)
            if cached_blog_post:
                return cached_blog_post

        # Use Gemini to search and write in one step
        prompt = f"""
        Please create a comprehensive blog post about "{topic}".
        
        First, search for recent articles and information about this topic using the DuckDuckGo tool.
        Then write a detailed blog post in New York Times style with:
        - Engaging headline
        - Multiple sections with clear headings
        - Key insights and takeaways
        - Proper citations of sources
        - Professional tone
        
        Topic: {topic}
        """
        
        try:
            response = self.gemini_agent.run(prompt)
            blog_post = response.content
            self._add_blog_post_to_cache(topic, blog_post)
            return blog_post
        except Exception as e:
            logger.error(f"Failed to generate blog post: {e}")
            return f"Failed to generate blog post for topic: '{topic}'. Error: {str(e)}"

    def _get_cached_blog_post(self, topic: str) -> Optional[str]:
        return self.session_state.get("blog_posts", {}).get(topic)

    def _add_blog_post_to_cache(self, topic: str, blog_post: Optional[str]) -> None:
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][topic] = blog_post

if __name__ == "__main__":
    from rich.prompt import Prompt

    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]\n")

    generate_blog_post = BlogPostGenerator()

    response = generate_blog_post.run(topic=topic, use_cache=False)
    print("\n" + "="*80)
    print("GENERATED BLOG POST:")
    print("="*80)
    print(response)