from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.media import Images
from agno.playground import playground, serve_playground_app

web_search_agent = Agent(
    name='Web Search Agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    description='An agent that can search the web and news from the web',
    system_message='reply in one sentence.',
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True,
)


# response = web_search_agent.run("Search for latest DeepSeek news.")
# print(response.content)

web_search_agent.print_response(
    message='Search for latest news related to the image',
    images=[
        # Image(url='<image_url>')
        Image(filepath='./resources/auto.png')
    ],
    stream=True
)

app = Playground(agents=[web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app('demo:app')
