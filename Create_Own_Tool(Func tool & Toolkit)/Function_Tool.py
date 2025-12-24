from agno.agent import Agent
from agno.models.openai import OpenAIChat

def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return str(a * b)

# Create the Agent and register the function as a tool
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[multiply_numbers]   # Registering the function directly
)

agent.print_response("What is seven times six?")
