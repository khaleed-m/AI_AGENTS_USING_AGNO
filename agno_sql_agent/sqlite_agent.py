from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.sql import SQLTools
from sqlalchemy import create_engine


engine = create_engine('sqlite:///./Chinook_Sqlite.sqlite')


agent = Agent(
    name='chinook SQLite agent',
    model=Ollama(id='llama3.2:3b'),
    markdown=True,
    system_message='You are equipped with tools to manage my SQLite database.',
    tools=[SQLTools(db_engine=engine)],
)
queries = [
    'list the tables',
    'how the sales are distributed over the different media types',
    'How many albums did Aerosmith release?',
    'Which artist has the highest number of tracks in the database?'
]

for query in queries:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    print('='*60)
    agent.print_response(query, stream=True)
    print("\n")