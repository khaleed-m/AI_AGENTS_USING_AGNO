import os
import requests
import json
from rich.prompt import Prompt
from rich.console import Console

console = Console()

class WorkingBlogGenerator:
    def __init__(self):
        self.groq_api_key = "your_groq_api_key_here"  # Get free key from https://console.groq.com/
        
    def generate_with_groq(self, prompt: str):
        """Generate content using Groq"""
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.groq_api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 3000,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            console.print(f"[red]Groq API error: {e}[/red]")
        return None
    
    def generate_blog_post(self, topic: str):
        """Generate comprehensive blog post using AI"""
        
        console.print("[yellow]Generating AI-powered blog post...[/yellow]")
        
        prompt = f"""Write a comprehensive, professional blog post about "{topic}".

REQUIREMENTS:
- 1200-1500 words
- SEO-optimized headline
- Clear section headings
- Professional, engaging tone
- Include real-world examples
- Add practical insights and tips
- Include relevant statistics (use realistic examples)
- Embed REAL, WORKING links from reputable sources like:
  * Official websites (apple.com, microsoft.com, etc.)
  * Industry publications (techcrunch.com, wired.com, etc.)
  * Research institutions (mit.edu, stanford.edu, etc.)
  * Government sites (.gov domains)
  * Professional organizations
- Use format: [descriptive text](https://actual-working-url.com)
- End with actionable takeaways

STRUCTURE:
1. Engaging introduction (150-200 words)
2. 4-6 main sections with subheadings (200-300 words each)
3. Real-world examples and use cases
4. Challenges and solutions
5. Future trends and predictions
6. Actionable takeaways
7. Strong conclusion
8. Resources section with REAL working links

IMPORTANT: Use only real, working URLs from reputable sources. Do not use example.com or placeholder links.

Write as an expert in the field. Make it publication-ready for Medium, LinkedIn, or company blogs.

Topic: {topic}

Blog Post:"""
        
        blog_content = self.generate_with_groq(prompt)
        
        if blog_content:
            console.print("[green]✓ Generated comprehensive blog using Groq AI[/green]")
            return blog_content
        else:
            return self.create_fallback_blog(topic)
    
    def create_fallback_blog(self, topic: str):
        """Fallback blog when AI fails"""
        return f"""# {topic.title()}: A Comprehensive Guide

## Introduction

{topic} has become increasingly important in today's digital landscape. This comprehensive guide explores the key aspects, benefits, challenges, and future trends related to {topic}.

## Overview of {topic}

{topic} represents a significant development in modern technology and business practices. Organizations worldwide are adopting {topic} to improve efficiency, reduce costs, and enhance user experiences.

## Key Benefits

The implementation of {topic} offers several advantages:
- Improved efficiency and productivity
- Cost reduction and resource optimization
- Enhanced user experience
- Better scalability and flexibility
- Competitive advantage in the market

## Current Trends

Recent developments in {topic} include:
- Increased adoption across industries
- Integration with emerging technologies
- Focus on user-centric approaches
- Emphasis on security and privacy
- Growing ecosystem of tools and platforms

## Challenges and Solutions

While {topic} offers many benefits, organizations face several challenges:
- Implementation complexity
- Resource requirements
- Training and skill development
- Integration with existing systems
- Maintaining security and compliance

## Future Outlook

The future of {topic} looks promising with continued innovation and adoption. Key trends to watch include:
- Advanced automation capabilities
- Better integration with AI and machine learning
- Improved user interfaces and experiences
- Enhanced security features
- Greater accessibility and affordability

## Actionable Takeaways

To get started with {topic}:
1. Assess your current needs and requirements
2. Research available solutions and platforms
3. Start with a pilot project or proof of concept
4. Invest in training and skill development
5. Plan for gradual implementation and scaling
6. Monitor progress and adjust strategies as needed

## Conclusion

{topic} continues to evolve and offer new opportunities for organizations and individuals. By understanding the key concepts, benefits, and challenges, you can make informed decisions about implementation and maximize the potential benefits.

## Resources and Further Reading

- [Official {topic} Documentation](https://developer.apple.com/ios/) (if applicable)
- [Industry Analysis Reports](https://www.gartner.com/)
- [Technical Research Papers](https://arxiv.org/)
- [Professional Community Forums](https://stackoverflow.com/)
- [Latest News and Updates](https://techcrunch.com/)
- [Best Practices Guides](https://www.smashingmagazine.com/)
- [Expert Insights and Blogs](https://medium.com/)
- [Official Training Resources](https://www.coursera.org/)
"""

def main():
    console.print("[bold cyan]🚀 Working Blog Generator[/bold cyan]")
    console.print("Uses Groq AI to generate comprehensive blog posts\n")
    
    topic = Prompt.ask("[bold]Enter a blog post topic[/bold]")
    
    generator = WorkingBlogGenerator()
    blog_post = generator.generate_blog_post(topic)
    
    console.print("\n" + "="*80)
    console.print("[bold green]GENERATED BLOG POST:[/bold green]")
    console.print("="*80)
    console.print(blog_post)
    
    # Save to file
    safe_topic = ''.join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()[:30]
    filename = f"blog_{safe_topic.lower().replace(' ', '_')}.md"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(blog_post)
        console.print(f"\n[green]✓ Blog post saved to: {filename}[/green]")
    except Exception as e:
        console.print(f"[red]Error saving file: {e}[/red]")

if __name__ == "__main__":
    main()