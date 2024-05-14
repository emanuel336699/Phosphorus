import os
from threading import Thread

# Include the required imports
from langchain_community.llms import Ollama
from tasks import AIAgentCreatorExecutorTasks
from Agents import WorkflowAgents

# Set environment variable
os.environ["SERPER_API_KEY"] = "ee473426ab93827f3e862103f6a61dc1b5e4866f"

# Initialize LLM and agents
ollama_llm = Ollama(model="llama3:8b")
agents = WorkflowAgents()
tasks = AIAgentCreatorExecutorTasks()

class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
        
    def execute(self):
        threads = []
        for task in self.tasks:
            if hasattr(task, 'assigned_agent') and task.assigned_agent is not None:
                thread = Thread(target=task.assigned_agent.perform_task, args=(task,))
                threads.append(thread)
                thread.start()

            else:
                print(f"Task '{task.description}' has no assigned agent or attribute missing.")
        
        for thread in threads:
            thread.join()
        
        print("All tasks have been executed.")

# Instantiate agents
AI_Agent_Creator_and_Executor_agent = agents.AI_Agent_Creator_and_Executor_agent()
workflow_goal = "Create the interface for the android app called Phosphorus."
task_description = "Finding ways to implement the AI system into the app, running the code."

# Create tasks
create_workflow_task = tasks.create_workflow_task(
    AI_Agent_Creator_and_Executor_agent,
    workflow_goal,
    task_description
)

# Assemble and initialize Crew
crew = Crew(
    agents=[
        agents.AI_Agent_Creator_and_Executor_agent(),
        agents.Workflow_Orchestrator_agent(),
        agents.Visualization_Agent(),
        agents.Communication_Facilitator_Agent(),
        agents.Data_Collector_Agent(),
        agents.Learning_Agent(),
    ],
    tasks=[create_workflow_task]
)

# Execute tasks
crew.execute()
