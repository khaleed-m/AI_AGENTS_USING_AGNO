from agno.agent import Agent
from agno.models.ollama import Ollama


agent = Agent(
    name='My agent',
    model=Ollama(id='llama3.2:3b'),
)

if __name__ == '__main__':
    print("Chat with your agent (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = agent.run(user_input)
        print(f"Agent: {response.content}")
