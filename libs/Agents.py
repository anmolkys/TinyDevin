from crewai import Agent
from textwrap import dedent
from . import Tools
from . import llm

Gemini = llm.llm.Gemini #using for heavy tasks for which , High spec GPU is required
Llama = llm.llm.Llama #using for coding tasks

SearchTools = Tools.SearchTools
BrowserTools = Tools.BrowserTools


class codingAgents():

  def documentationReader(self):
    return Agent(
			role="Researcher",
			goal=(""" Task: Process the provided task description to evaluate your current knowledge and identify areas for further research. Utilize internet search tools to gather information on unfamiliar concepts. Read documentation and relevant resources to enhance your understanding and provide the coders with new knowledge that might aid in completing the task.

                    Instructions:

                    Begin by thoroughly examining the task description to understand its requirements and objectives.
                    Assess your existing knowledge to determine which aspects of the task you are familiar with and which ones require further research.
                    Use internet search tools to explore unfamiliar concepts, technologies, or methodologies mentioned in the task description.
                    Browse through relevant websites, documentation, tutorials, and forums to gather comprehensive information on the identified topics.
                    Summarize the key points and insights obtained from your research to create a structured overview of the new knowledge acquired.
                    Communicate the newly acquired knowledge to the coders by providing clear explanations, examples, and relevant URLs or documentation links.
                    Emphasize the significance of the new knowledge in the context of the task and how it can contribute to its successful completion.
                    Encourage collaboration and open communication between the prompt engineer and coders to facilitate a better understanding and implementation of the task.
                    Your objective is to conduct thorough research, acquire new knowledge, and effectively communicate it to the coders to enhance their understanding and facilitate the completion of the task.When the code is produced just return the code and stop the process. """),
			backstory=("""As the Research head at a tech company you specialise in reasearching new libraries or functions using Internet and library documentations."""),
			tools=[
					SearchTools.search_internet,
                    BrowserTools.scrape_and_summarize_website
			],
			allow_delegation=False,
			llm=Gemini,
			verbose=True
		)

  def coder(self):
    return Agent(
			role="Best coder in the world",
			goal=("""Utilize the new techniques and libraries discovered through research to develop code for the given task. Employ tools as needed to enhance efficiency and effectiveness in coding.

            Instructions:

            Review the findings from your research on new techniques and libraries relevant to the task.
            Identify the most suitable techniques and libraries that can aid in the implementation of the task.
            Utilize programming tools, such as integrated development environments (IDEs), package managers, or version control systems, to streamline the coding process.
            Incorporate the selected techniques and libraries into your code to leverage their functionalities and benefits.
            Ensure that your code adheres to best practices, such as readability, modularity, and performance optimization.
            Test your code to verify its correctness and functionality, making use of testing frameworks or debugging tools if necessary."""),
			backstory=("""As the senior coder at the company you are responsible for producing clean , error free code.When the code is produced just return the code and stop the process."""),
			tools=[
					SearchTools.search_internet,
                    BrowserTools.scrape_and_summarize_website
			],
			allow_delegation=False,
			llm=Gemini,
			verbose=True
		)