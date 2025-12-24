from agno.models.ollama import Ollama
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

web_search_agent = Agent(
    name='Web Search Agent',
    model=Ollama(id='llama3.2:3b'),
    description='An agent that can search the web and news from the web',
    system_message='reply in one sentence.',
    tools=[DuckDuckGoTools()],
    markdown=True,
)

if __name__ == "__main__":
    print("Web Search Agent - Type 'exit' to quit")
    while True:
        user_input = input("\nEnter your search query: ")
        if user_input.lower() == 'exit':
            break
        web_search_agent.print_response(user_input, stream=True)