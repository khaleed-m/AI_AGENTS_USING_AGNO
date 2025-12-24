import os
import requests
import json
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.prompt import Prompt
from rich.console import Console

console = Console()

class AdvancedBlogGenerator:
    def __init__(self):
        # Free API options - add your keys here
        self.groq_api_key = "your_groq_api_key_here"  # Get free key from https://console.groq.com/
        self.huggingface_token = "your_hf_token_here"  # Free: https://huggingface.co/settings/tokens
        
    def search_related_content(self, subtopics: list):
        """Search for additional content based on subtopics"""
        all_results = []
        search_tool = DuckDuckGoTools()
        
        for subtopic in subtopics:
            try:
                console.print(f"[dim]Searching for: {subtopic}[/dim]")
                results = search_tool.duckduckgo_search(subtopic, max_results=3)
                if results:
                    all_results.extend(results)
            except Exception as e:
                console.print(f"[dim red]Search error for {subtopic}: {e}[/dim red]")
        
        return all_results
    
    def generate_content_outline(self, topic: str):
        """Generate comprehensive content outline with subtopics"""
        outline_prompt = f"""Create a comprehensive blog post outline for "{topic}". 
        
Provide:
1. Main sections (4-6 sections)
2. Key subtopics to research
3. Important aspects to cover

Format your response as:
SECTIONS:
- Section 1 title
- Section 2 title
...

SUBTOPICS TO RESEARCH:
- subtopic 1
- subtopic 2
...

Topic: {topic}"""
        
        outline = self.generate_with_groq(outline_prompt)
        if not outline:
            # Fallback outline
            return {
                'sections': [f"{topic} Overview", f"Current Trends in {topic}", f"Key Benefits", f"Challenges", f"Future Outlook"],
                'subtopics': [f"{topic} trends 2024", f"{topic} benefits", f"{topic} challenges", f"{topic} future"]
            }
        
        # Parse the outline
        sections = []
        subtopics = []
        
        lines = outline.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if 'SECTIONS:' in line.upper():
                current_section = 'sections'
            elif 'SUBTOPICS' in line.upper():
                current_section = 'subtopics'
            elif line.startswith('-') and current_section:
                content = line[1:].strip()
                if current_section == 'sections':
                    sections.append(content)
                elif current_section == 'subtopics':
                    subtopics.append(content)
        
        return {'sections': sections, 'subtopics': subtopics}
    
    def generate_with_groq(self, prompt: str):
        """Generate content using Groq (Free Llama models)"""
        if not self.groq_api_key or self.groq_api_key == "your_groq_api_key_here":
            return None
            
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.groq_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3-8b-8192",  # Free model
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            console.print(f"[red]Groq API error: {e}[/red]")
        return None
    
    def generate_with_huggingface(self, prompt: str):
        """Generate content using Hugging Face (Free models)"""
        if not self.huggingface_token or self.huggingface_token == "your_hf_token_here":
            return None
            
        # Using free Mistral model
        url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
        headers = {"Authorization": f"Bearer {self.huggingface_token}"}
        
        data = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 1000,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get("generated_text", "")
        except Exception as e:
            console.print(f"[red]Hugging Face API error: {e}[/red]")
        return None
    
    def create_enhanced_blog_prompt(self, topic: str, outline: dict, search_results: list):
        """Create enhanced prompt with outline and comprehensive research"""
        
        # Organize search results by relevance
        articles_text = ""
        links_list = []
        
        for i, result in enumerate(search_results[:10], 1):
            if isinstance(result, dict):
                title = result.get('title', 'No title')
                snippet = result.get('body', result.get('snippet', 'No description'))
                url = result.get('url', '')
                articles_text += f"\n{i}. {title}\n{snippet}\nURL: {url}\n"
                links_list.append(f"[{title}]({url})")
        
        sections_text = "\n".join([f"- {section}" for section in outline.get('sections', [])])
        
        prompt = f"""Write a comprehensive, professional blog post about "{topic}" using the following structure and research:

SUGGESTED SECTIONS:
{sections_text}

RESEARCH SOURCES:
{articles_text}

AVAILABLE LINKS (use these naturally in content):
{', '.join(links_list[:8])}

INSTRUCTIONS:
1. Create an engaging, SEO-optimized headline
2. Write a compelling introduction (150-200 words)
3. Develop each section with:
   - Clear subheadings
   - Detailed explanations (200-300 words per section)
   - Real examples and data from sources
   - Naturally embedded links using [text](url) format
4. Include practical insights and actionable advice
5. Add statistics, trends, and expert opinions from the sources
6. Write in professional, engaging tone for business/tech audience
7. Create a strong conclusion with key takeaways
8. Add a "Resources and Further Reading" section with organized links
9. Target 1200-1500 words total
10. Ensure all claims are backed by the provided sources

Generate comprehensive, original content that goes beyond just summarizing the sources. Provide analysis, insights, and practical value.

Topic: {topic}

Blog Post:"""
        
        return prompt
    
    def generate_blog_post(self, topic: str):
        """Generate advanced blog post with comprehensive research"""
        
        # Step 1: Generate content outline and subtopics
        console.print("[yellow]Creating content outline...[/yellow]")
        outline = self.generate_content_outline(topic)
        
        # Step 2: Search for main topic
        console.print(f"[bold blue]Searching for main topic: {topic}[/bold blue]")
        search_tool = DuckDuckGoTools()
        main_results = []
        try:
            main_results = search_tool.duckduckgo_search(topic, max_results=5)
        except Exception as e:
            console.print(f"[red]Main search error: {e}[/red]")
        
        # Step 3: Search for related subtopics
        console.print("[yellow]Searching for related content...[/yellow]")
        related_results = self.search_related_content(outline.get('subtopics', []))
        
        # Combine all results
        all_results = (main_results or []) + (related_results or [])
        
        if not all_results:
            return "No search results found. Please try a different topic."
        
        # Step 4: Generate comprehensive blog post
        console.print("[yellow]Generating comprehensive AI blog post...[/yellow]")
        prompt = self.create_enhanced_blog_prompt(topic, outline, all_results)
        
        # Try AI generation
        blog_content = self.generate_with_groq(prompt)
        if blog_content:
            console.print("[green]✓ Generated comprehensive blog using Groq AI[/green]")
            return blog_content
        
        # Fallback
        console.print("[yellow]AI unavailable, using enhanced simple version...[/yellow]")
        return self.create_enhanced_simple_blog(topic, outline, all_results)
    
    def create_enhanced_simple_blog(self, topic: str, outline: dict, search_results: list):
        """Enhanced fallback blog creation with better structure"""
        sections = outline.get('sections', [f"{topic} Overview", "Key Insights", "Current Trends", "Conclusion"])
        
        blog_post = f"""# {topic.title()}: Comprehensive Guide and Latest Insights

## Introduction
This comprehensive guide explores {topic}, covering the latest developments, trends, and insights based on current research and industry analysis.

"""
        
        # Distribute search results across sections
        results_per_section = len(search_results) // len(sections) + 1
        
        for i, section in enumerate(sections):
            blog_post += f"## {section}\n\n"
            
            # Add relevant results for this section
            start_idx = i * results_per_section
            end_idx = start_idx + results_per_section
            section_results = search_results[start_idx:end_idx]
            
            for result in section_results:
                if isinstance(result, dict):
                    title = result.get('title', 'No title')
                    url = result.get('url', 'No URL')
                    snippet = result.get('body', result.get('snippet', 'No description'))
                    
                    blog_post += f"{snippet}\n\nAccording to [this research]({url}), these findings highlight important aspects of {topic}. "
                    blog_post += f"For more detailed information, you can [explore the full analysis here]({url}).\n\n"
        
        # Add resources section
        blog_post += "## Resources and Further Reading\n\n"
        for i, result in enumerate(search_results[:8], 1):
            if isinstance(result, dict):
                title = result.get('title', 'No title')
                url = result.get('url', 'No URL')
                blog_post += f"{i}. [{title}]({url})\n"
        
        return blog_post

def main():
    console.print("[bold cyan]🚀 Advanced AI Blog Post Generator[/bold cyan]")
    console.print("Supports: Groq (Free), Hugging Face (Free), and Fallback mode\n")
    
    # Setup instructions
    console.print("[yellow]Setup Instructions:[/yellow]")
    console.print("1. Get free Groq API key: https://console.groq.com/")
    console.print("2. Get free Hugging Face token: https://huggingface.co/settings/tokens")
    console.print("3. Add your keys to the code\n")
    
    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]")
    
    generator = AdvancedBlogGenerator()
    blog_post = generator.generate_blog_post(topic)
    
    console.print("\n" + "="*80)
    console.print("[bold green]GENERATED BLOG POST:[/bold green]")
    console.print("="*80)
    console.print(blog_post)
    
    # Save to file
    safe_topic = ''.join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()[:50]
    filename = f"blog_post_{safe_topic.lower().replace(' ', '_')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(blog_post)
    console.print(f"\n[green]✓ Blog post saved to: {filename}[/green]")

if __name__ == "__main__":
    main()