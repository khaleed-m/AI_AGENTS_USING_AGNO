from agno.tools.duckduckgo import DuckDuckGoTools
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def generate_blog_post(topic: str):
    """Generate a simple blog post using DuckDuckGo search results"""
    
    console.print(f"[bold blue]Searching for articles about: {topic}[/bold blue]")
    
    # Initialize DuckDuckGo search
    search_tool = DuckDuckGoTools()
    
    try:
        # Search for articles
        search_results = search_tool.duckduckgo_search(topic, max_results=5)
        
        if not search_results:
            return f"No search results found for topic: '{topic}'"
        
        # Generate a simple blog post
        blog_post = f"""
# {topic.title()}: Latest Insights and Updates

## Introduction
This blog post explores the latest developments and insights about {topic}, based on recent search results and available information.

## Key Findings

"""
        
        # Add search results as content with embedded links
        references = []
        for i, result in enumerate(search_results[:5], 1):
            if isinstance(result, dict):
                title = result.get('title', 'No title')
                url = result.get('url', 'No URL')
                snippet = result.get('body', result.get('snippet', 'No description'))
                
                # Add to references list
                references.append(f"[{i}] {title} - {url}")
                
                blog_post += f"""
### {i}. {title}

{snippet}

According to [this source]({url}), the information highlights key aspects of {topic}. For more detailed insights, you can [read the full article here]({url}).

"""
        
        # Add references section
        blog_post += """
## Useful Links and Resources

Here are some valuable links related to {topic}:

""".format(topic=topic)
        
        for ref in references:
            blog_post += f"- {ref}\n"
        
        blog_post += """
## Conclusion

Based on the search results above, {topic} continues to be a topic of significant interest and development. The information gathered provides valuable insights into current trends and developments in this area.

## References

All information in this blog post is sourced from the search results listed above. For the most current information, please refer to the original sources.
""".format(topic=topic)
        
        return blog_post
        
    except Exception as e:
        return f"Error generating blog post: {str(e)}"

if __name__ == "__main__":
    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]")
    
    console.print("\n[yellow]Generating blog post...[/yellow]")
    
    blog_post = generate_blog_post(topic)
    
    console.print("\n" + "="*80)
    console.print("[bold green]GENERATED BLOG POST:[/bold green]")
    console.print("="*80)
    console.print(blog_post)