'''
CREW.AI framework for managing agents and workflows.
'''
class Agent:
    '''
    Class representing an agent in the Phosphorus system.
    '''
    def __init__(self, name):
        '''
        Initialize the agent with the given name.
        '''
        self.name = name
        self.role = None
        self.task = None
    def set_role(self, role):
        '''
        Set the role of the agent.
        '''
        self.role = role
    def assign_task(self, task):
        '''
        Assign a task to the agent.
        '''
        self.task = task
class Workflow:
    '''
    Class representing a workflow in the Phosphorus system.
    '''
    def __init__(self):
        '''
        Initialize the workflow with an empty list of agents.
        '''
        self.agents = []
    def add_agent(self, agent):
        '''
        Add an agent to the workflow.
        '''
        self.agents.append(agent)
    def run(self):
        '''
        Run the workflow by executing tasks assigned to agents.
        '''
        for agent in self.agents:
            print(f"Agent {agent.name} with role {agent.role} is executing task: {agent.task}")