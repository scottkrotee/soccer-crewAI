from crewai import Agent, Task, Crew, Process
import os
 
os.environ["OPENAI_API_KEY"] = "YOUR KEY"

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

event_researcher = Agent(
    role='Event Researcher',
    goal='Find all NCAA and professional soccer combines or tryouts in 2024',
    backstory='You are an AI soccer event researcher for my agents',
    verbose=True,
  allow_delegation=False,
  tools=[search_tool]
    
)

event_reporter = Agent(
    role='Event Reporter',
    goal='Report all upcoming NCAA and professional soccer combines or tryouts',
    backstory='You are an AI event reporter who specializes in organizing calanders',
    verbose=True,
  allow_delegation=True,
)

task1 = Task(description='Find me all upcoming NCAA and professional soccer combines or tryouts in 2024.', agent=event_researcher)
task2 = Task(description='Report all upcoming professional soccer combines or tryouts in an organized calander.', agent=event_reporter)


crew = Crew(
    agents=[event_researcher, event_reporter],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()

print("######################")
print(result)