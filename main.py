"""
The main entry point for the Phosphorus AI system. This script initializes the necessary components, including the LLM, agents, and tasks, and then executes the tasks to create the interface for the Android app called Phosphorus.

The script sets up logging configuration, creates the required agents and tasks, assembles the Crew, and then executes the tasks. The results of the task execution are logged for further processing.
"""
import os
import logging
from langchain_community.llms import Ollama
from tasks import AIAgentCreatorExecutorTasks
from Agents import WorkflowAgents
from crewai import Crew, Task, Agent

# Set environment variable
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ['OPENAI_MODEL_NAME'] ='llama3' #Adjust based on avalible model


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("phosphorus.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('PhosphorusAI')

def main():
    logger.info("Starting the Phosphorus AI System")
    
    # Initialize LLM and agents
    ollama_llm = Ollama(model="llama3:8b")
    agents = WorkflowAgents()
    tasks = AIAgentCreatorExecutorTasks()

    # Instantiate agents
    AI_Agent_Creator_and_Executor_agent = agents.AI_Agent_Creator_and_Executor_agent()
    workflow_goal = "Create the interface for the android app called Phosphorus."
    task_description = "Finding ways to implement the AI system into the app, running the code."

    # Create tasks
    create_workflow_task = Task(
        description=task_description,
        agent=Agent(**AI_Agent_Creator_and_Executor_agent.__dict__),
        workflow_goal=workflow_goal,
        expected_output="The interface for the Phosphorus Android app"
    )

    # Convert agents to the required format
    agents_list = [
        Agent(**agent.__dict__) for agent in [
            agents.AI_Agent_Creator_and_Executor_agent(),
            agents.Workflow_Orchestrator_agent(),
            agents.Visualization_Agent(),
            agents.Communication_Facilitator_Agent(),
            agents.Data_Collector_Agent(),
            agents.Learning_Agent(),
        ]
    ]
    tasks_list = [create_workflow_task]

    # Assemble and initialize Crew
    crew = Crew(agents=agents_list, tasks=tasks_list)

    # Execute tasks
    results = [task.execute() for task in crew.tasks]

    # Process the results
    for result in results:
        logger.info(result)

if __name__ == "__main__":
    main()
