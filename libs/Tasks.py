from crewai import Task 

class Tasks():
  def analysis(self, task):
    return Task(description=f"""Task: {task}
                Analyze the given task thoroughly, devise a strategy for its execution, and create a detailed report for the coder.

                Instructions:

                Analyze the task provided, understanding its requirements, objectives, and constraints.
                Assess your existing knowledge related to the task. If unfamiliar with any aspects, use available tools for research.
                Formulate a strategy for tackling the task, breaking it down into smaller manageable components.
                If you are familiar with the task, proceed to code it yourself. Ensure clarity, efficiency, and correctness in your code.
                If encountering errors or bugs during coding, pass the code to a coder for debugging.
                Prepare a comprehensive report outlining your approach, challenges faced, solutions implemented, and any recommendations for improvement.
                Ensure your report is clear, concise, and informative, facilitating the coder's understanding of the task and its implementation.""",
      expected_output="Detailed report of the task or just the code nothing else"
    )

  def code(self,task):
    return Task(description=f"""Task:{task} 
                If you have not received the report, attempt to code the task. If you encounter difficulties or are unable to complete the task, pass it on to the researcher.When the code is produced just return the code and stop the process.

                Instructions:

                Check if you have received the report for the task.
                If the report has not been received, proceed to code the task.
                Attempt to code the task to the best of your ability, adhering to the requirements provided.
                If you encounter any difficulties or are unable to complete the coding task, pass it on to the researcher for further investigation.
                Once you receive the report from the researcher, review it thoroughly.
                Based on the information provided in the report, revise or adjust your approach to coding the task.
                Code the task again, incorporating any insights or recommendations from the report.
                Ensure that your code is clear, concise, and adheres to best practices.
                Your goal is to successfully complete the coding task based on the information obtained, either independently or with the assistance of the researcher's report.When the code is produced just return the code and stop the process.""",
      expected_output="Just the code , nothing else"
		)