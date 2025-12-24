from advanced_blog_generator import AdvancedBlogGenerator
from rich.console import Console

console = Console()

def demo():
    console.print("[bold cyan]🚀 Blog Generator Demo[/bold cyan]\n")
    
    # Example topics that work well
    example_topics = [
        "AI in Healthcare",
        "Remote Work Productivity",
        "Blockchain Technology", 
        "Digital Marketing Trends",
        "Cybersecurity Best Practices",
        "Cloud Computing Benefits",
        "Machine Learning Applications",
        "Social Media Marketing"
    ]
    
    console.print("[yellow]✅ CORRECT: Enter simple topics like these:[/yellow]")
    for topic in example_topics:
        console.print(f"   • {topic}")
    
    console.print("\n[red]❌ WRONG: Don't enter long instructions or prompts[/red]")
    console.print("   • Generate a professional blog...")
    console.print("   • Requirements: 1200+ words...")
    console.print("   • You are a professional writer...")
    
    console.print("\n[bold green]Let's try with a working example:[/bold green]")
    
    # Demo with a working topic
    generator = AdvancedBlogGenerator()
    topic = "AI in Healthcare"
    
    console.print(f"[blue]Generating blog for: '{topic}'[/blue]")
    blog_post = generator.generate_blog_post(topic)
    
    console.print("\n" + "="*60)
    console.print("[bold green]GENERATED BLOG POST:[/bold green]")
    console.print("="*60)
    print(blog_post[:500] + "..." if len(blog_post) > 500 else blog_post)
    
    # Save demo
    with open("demo_blog_post.md", "w", encoding="utf-8") as f:
        f.write(blog_post)
    console.print(f"\n[green]✅ Full blog saved to: demo_blog_post.md[/green]")

if __name__ == "__main__":
    demo()