from agno.models.ollama import Ollama
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
import json
from datetime import datetime

console = Console()

class AdvancedWebSearchAgent:
    def __init__(self):
        self.agent = Agent(
            name='Advanced Web Search Agent',
            model=Ollama(id='llama3.2:3b'),
            description='An intelligent web search agent with advanced capabilities',
            system_message='''You are an advanced web search assistant. 
            - Provide comprehensive and accurate information
            - Cite sources when possible
            - Summarize key findings
            - Offer follow-up suggestions''',
            tools=[DuckDuckGoTools()],
            markdown=True,
        )
        self.search_history = []
    
    def display_welcome(self):
        welcome_text = """
# 🔍 Advanced Web Search Agent

Welcome to the Advanced Web Search Agent! I can help you with:

- **Web Search**: Search for current information on any topic
- **News Search**: Find latest news and updates
- **Research**: Comprehensive research on complex topics
- **Fact Checking**: Verify information and claims
- **Trend Analysis**: Discover trending topics and insights

**Commands:**
- Type your search query naturally
- Use 'history' to see search history
- Use 'clear' to clear history
- Use 'help' for more commands
- Use 'exit' to quit
        """
        console.print(Panel(Markdown(welcome_text), title="🚀 Advanced Search Agent", border_style="blue"))
    
    def save_search(self, query, response):
        search_entry = {
            'timestamp': datetime.now().isoformat(),
            'query': query,
            'response_preview': response[:200] + "..." if len(response) > 200 else response
        }
        self.search_history.append(search_entry)
    
    def show_history(self):
        if not self.search_history:
            console.print("📝 No search history yet.", style="yellow")
            return
        
        console.print("\n📚 Search History:", style="bold blue")
        for i, entry in enumerate(self.search_history[-10:], 1):  # Show last 10
            timestamp = datetime.fromisoformat(entry['timestamp']).strftime("%H:%M:%S")
            console.print(f"{i}. [{timestamp}] {entry['query']}", style="cyan")
    
    def show_help(self):
        help_text = """
# 🆘 Help Commands

**Search Commands:**
- `news about [topic]` - Search for latest news
- `research [topic]` - Deep research on a topic
- `trends in [field]` - Find trending topics
- `compare [A] vs [B]` - Compare two things

**Utility Commands:**
- `history` - Show search history
- `clear` - Clear search history
- `help` - Show this help
- `exit` - Quit the application

**Examples:**
- "What's the latest news about AI?"
- "Research renewable energy trends"
- "Compare Python vs JavaScript"
        """
        console.print(Panel(Markdown(help_text), title="📖 Help Guide", border_style="green"))
    
    def process_query(self, query):
        # Add query enhancement based on keywords
        if query.lower().startswith('news'):
            enhanced_query = f"Latest news: {query[4:].strip()}"
        elif query.lower().startswith('research'):
            enhanced_query = f"Comprehensive research on: {query[8:].strip()}"
        elif query.lower().startswith('trends'):
            enhanced_query = f"Current trends and analysis: {query[6:].strip()}"
        elif query.lower().startswith('compare'):
            enhanced_query = f"Detailed comparison: {query[7:].strip()}"
        else:
            enhanced_query = query
        
        return enhanced_query
    
    def run(self):
        self.display_welcome()
        
        while True:
            try:
                query = Prompt.ask("\n🔍 [bold cyan]Enter your search query[/bold cyan]")
                
                if query.lower() == 'exit':
                    console.print("👋 Goodbye! Thanks for using Advanced Web Search Agent!", style="bold green")
                    break
                elif query.lower() == 'history':
                    self.show_history()
                    continue
                elif query.lower() == 'clear':
                    self.search_history.clear()
                    console.print("🗑️ Search history cleared!", style="yellow")
                    continue
                elif query.lower() == 'help':
                    self.show_help()
                    continue
                elif not query.strip():
                    console.print("⚠️ Please enter a valid search query.", style="red")
                    continue
                
                # Process and enhance the query
                enhanced_query = self.process_query(query)
                
                # Show processing indicator
                with console.status("[bold green]Searching the web...", spinner="dots"):
                    response = self.agent.run(enhanced_query)
                
                # Display results
                console.print(f"\n🎯 [bold]Results for:[/bold] {query}")
                console.print("─" * 60)
                
                if response and response.content:
                    console.print(Markdown(response.content))
                    self.save_search(query, response.content)
                else:
                    console.print("❌ No results found. Please try a different query.", style="red")
                
                console.print("─" * 60)
                
            except KeyboardInterrupt:
                console.print("\n\n👋 Goodbye! Thanks for using Advanced Web Search Agent!", style="bold green")
                break
            except Exception as e:
                console.print(f"❌ Error: {str(e)}", style="red")

if __name__ == "__main__":
    agent = AdvancedWebSearchAgent()
    agent.run()