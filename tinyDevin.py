from libs.Tasks import Tasks
from libs.Agents import codingAgents
from crewai import Crew
from crewai.process import Process
from libs.llm import llm

Gemini = llm.Gemini
Llama = llm.Llama

#We can use LLama as well but Gemini is better at managing

tasks = Tasks()
agents = codingAgents()
task = "write a linkedlist in Julia"
researcher = agents.documentationReader()
coder = agents.coder()
research_task = tasks.analysis(task)
coding_task = tasks.code(task)

tinyDevin = Crew(
	agents=[researcher,coder],
	tasks=[research_task,coding_task],
	verbose=False,
  process=Process.hierarchical,
  manager_llm = Gemini
)


code = tinyDevin.kickoff()

print("Here is your code: ")
print(code)