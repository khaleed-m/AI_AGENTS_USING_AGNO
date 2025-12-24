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
    'Execute this SQL: SELECT name FROM sqlite_master WHERE type="table"',
    'Execute this SQL: SELECT mt.Name as MediaType, SUM(il.UnitPrice * il.Quantity) as TotalSales FROM InvoiceLine il JOIN Track t ON il.TrackId = t.TrackId JOIN MediaType mt ON t.MediaTypeId = mt.MediaTypeId GROUP BY mt.Name',
    'Execute this SQL: SELECT COUNT(*) as AlbumCount FROM Album al JOIN Artist ar ON al.ArtistId = ar.ArtistId WHERE ar.Name = "Aerosmith"',
    'Execute this SQL: SELECT ar.Name, COUNT(t.TrackId) as TrackCount FROM Artist ar JOIN Album al ON ar.ArtistId = al.ArtistId JOIN Track t ON al.AlbumId = t.AlbumId GROUP BY ar.Name ORDER BY TrackCount DESC LIMIT 1'
]

for query in queries:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    print('='*60)
    agent.print_response(query, stream=True)
    print("\n")