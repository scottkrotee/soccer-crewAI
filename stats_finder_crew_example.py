from crewai import Agent, Task, Crew, Process
import os
 
os.environ["OPENAI_API_KEY"] = "YOUR KEY"

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

database_researcher = Agent(
    role='Database Researcher',
    goal='Find useful databases for my agents in soccer statistics',
    backstory='You are an AI database researcher for my agents',
    verbose=True,
  allow_delegation=False,
  tools=[search_tool]    
)

researcher = Agent(
    role='Researcher',
    goal='Find statistics on soccer players',
    backstory='You are an AI statistics reseacher',
    verbose=True,
  allow_delegation=False,
  tools=[search_tool]    
)

reporter = Agent(
    role='Reporter',
    goal='Report accurate statistics on soccer players',
    backstory='You are an AI statistics reporter who specializes in reporting sports statistics',
    verbose=True,
    allow_delegation=False
)

task1 = Task(description='Find me all useful soccer databases for my agents.', agent=database_researcher)
task2 = Task(description='Find me all individual player statistics for Scott Krotee using the databases found by the Database Researcher.', agent=researcher)
task3 = Task(description='Report all individual player statistics for Scott Krotee from the Researcher', agent=reporter)

crew = Crew(
    agents=[database_researcher, researcher, reporter],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()

print("######################")
print(result)