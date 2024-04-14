'''
Main file for the Phosphorus agent system.
'''
from crewai import Agent, Workflow
def create_agent(agent_name, agent_role):
    '''
    Function to create a new agent with the given name and role.
    '''
    agent = Agent(agent_name)
    agent.set_role(agent_role)
    return agent
def assign_task(agent, task):
    '''
    Function to assign a task to an agent.
    '''
    agent.assign_task(task)
def main():
    '''
    Main function to run the Phosphorus agent system.
    '''
    # Create a workflow
    workflow = Workflow()
    # Create agents
    agent1 = create_agent("Agent1", "Coding")
    agent2 = create_agent("Agent2", "Running Code and Debugging")
    # Assign tasks to agents
    assign_task(agent1, "Code the interface for the Phosphorus App")
    assign_task(agent2, "Assist Agent 1 in Coding but especially Running And Debbuging, reflecting on all issues you stumble upon togheder")
    # Add agents to the workflow
    workflow.add_agent(agent1)
    workflow.add_agent(agent2)
    # Run the workflow
    workflow.run()
if __name__ == "__main__":
    main()