from agno.agent import Agent
from agno.models.openai import OpenAIChat
from math_Tookit import MathToolkit

# Create the Agent and attach the MathToolkit
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[MathToolkit()]
)

agent.print_response("What is 15 - 3")
