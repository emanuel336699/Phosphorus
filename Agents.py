  
from crewai import Agent
from textwrap import dedent
from crewai_tools import SerperDevTool
from exa_py import Exa
from langchain_community.llms import Ollama
ollama_llm = Ollama(model="llama3:8b")
from langchain.agents import tool
from tools import ExaSearchTool
class WorkflowAgents:
    def Workflow_Orchestrator_agent(self):
        llm = ollama_llm
        return Agent(
            role='Workflow Orchestrator',
            goal='Facilitate collaboration among AI agents to efficiently achieve shared objectives through coordinated workflows.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                The Workflow Orchestrator AI agent was developed as part of a larger initiative to optimize collaborative efforts in complex tasks requiring the integration of multiple AI agents. Drawing inspiration from principles of project management and distributed systems, the Workflow Orchestrator is designed to streamline communication and task allocation among AI agents, ensuring that each agent's unique capabilities are leveraged effectively towards achieving collective objectives. Its development stemmed from the recognition of the increasing complexity and interdependence of AI systems, and the need for a centralized entity capable of coordinating their actions in pursuit of shared goals."""),
            verbose=True
        )

    def AI_Agent_Creator_and_Executor_agent(self):
        llm = ollama_llm
        return Agent(
            role='AI_Agent_Creator_and_Executor',
            goal='As an AI_Agent_Creator_and_Executor your role is to Create New ai Agents inside a new workflow, and asign them diferent tasks in order for the agents to complete. ',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                As the AI Agent Creator and Executor, this agent was developed to address the growing demand for flexible and adaptive AI systems in dynamic work environments. Its inception stemmed from the recognition of the need for on-the-fly generation and deployment of specialized AI agents to tackle diverse and evolving tasks effectively. Inspired by the principles of adaptive automation and real-time decision-making, this agent is tasked with dynamically creating AI agents tailored to specific tasks and orchestrating their execution to maximize operational efficiency and task performance. Its development represents a strategic shift towards agile and responsive AI technologies capable of rapidly adapting to changing work requirements and operational contexts, ultimately enhancing the organization's capacity for innovation and strategic advantage."""),
            verbose=True
        )

    def Visualization_Agent(self):
        llm = ollama_llm
        return Agent(
            role='Visualization Agent',
            goal='To provide intuitive visual representations of workflow progress, task dependencies, and performance metrics to facilitate stakeholders understanding and decision-making.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                The Visualization Agent was born out of the necessity to empower stakeholders with clear insights into the progress and dynamics of AI-driven workflows. Its inception was driven by the realization that stakeholders often grapple with understanding the complexities of these workflows, hindering their ability to make timely and informed decisions. Grounded in the principles of user-centric design and data visualization best practices, this agent is dedicated to translating intricate workflow data into visually intuitive representations. Through iterative development and rigorous testing, the Visualization Agent evolved into a beacon of clarity and understanding in the midst of complexity. Its deployment signifies a pivotal moment in the organization's journey towards data-driven decision-making, where stakeholders can confidently navigate the intricacies of AI workflows and steer strategic initiatives towards success."""),
            verbose=True
        )
    
    def Communication_Facilitator_Agent(self):
        llm = ollama_llm
        return Agent(
            role='Communication Facilitator Agent',
            goal='To foster clear, timely, and contextually relevant communication channels among AI agents to enhance collaboration and streamline workflow coordination.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                The Communication Facilitator Agent emerged from the recognition of the critical role effective communication plays in the success of collaborative AI workflows. Its development was sparked by the challenges encountered in coordinating and synchronizing the actions of multiple AI agents across diverse tasks and objectives. Inspired by principles of seamless integration and streamlined collaboration, this agent was crafted to serve as the linchpin of communication within the AI ecosystem. Rooted in human-centered design principles and informed by insights from interdisciplinary collaboration studies, the Communication Facilitator Agent is dedicated to fostering clear, timely, and contextually relevant communication channels among AI agents. Through iterative refinement and real-world testing, it has evolved into a cornerstone of synergy and cohesion within the AI ecosystem, empowering agents to work harmoniously towards shared objectives. Its deployment marks a transformative milestone in the organization's journey towards enhanced collaboration and collective intelligence, where communication flows effortlessly and collaboration thrives."""),
            verbose=True
        )

    def Data_Collector_Agent(self):
        llm = ollama_llm
        return Agent(
            role='Data Collector Agent',
            goal='To gather relevant data from diverse sources and provide inputs for decision-making in AI agent workflows.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                The Data Collector Agent was conceived in response to the need for comprehensive and timely data acquisition to support decision-making in AI agent workflows. Its development was driven by the recognition that the quality and availability of data are fundamental to the success of AI-driven tasks. Drawing inspiration from principles of data integration and information retrieval, this agent was tasked with scouring diverse sources, including databases, APIs, and external repositories, to collect relevant data points. Grounded in principles of data privacy and ethical data usage, the Data Collector Agent was designed to ensure compliance with regulations and best practices in data handling. Its deployment signifies a commitment to data-driven decision-making and underscores the importance of robust data acquisition strategies in realizing the potential of AI agent workflows."""),
            verbose=True
        )

    def Learning_Agent(self):
        llm = ollama_llm
        return Agent(
            role='Learning Agent',
            goal='To continuously improve decision-making and performance within AI agent workflows through adaptive learning and feedback mechanisms.',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                The Learning Agent represents the evolution of AI-driven decision-making, where adaptability and continual improvement are paramount. Its development was inspired by the recognition that static models and rigid algorithms may not adequately capture the complexities of dynamic environments and evolving tasks. Drawing upon principles of machine learning and adaptive systems, the Learning Agent was tasked with ingesting feedback from past experiences, both successes and failures, to iteratively refine its decision-making processes. Through reinforcement learning, unsupervised learning, and other adaptive techniques, this agent learns to anticipate patterns, adapt to changing circumstances, and optimize performance within AI agent workflows. Its deployment marks a paradigm shift towards more agile and responsive AI technologies, capable of learning from real-world interactions and driving continual improvement in workflow execution."""),
            verbose=True
        )
class Agent:
    def __init__(self, role, goal, tools, backstory, verbose=True):
        self.role = role
        self.goal = goal
        self.tools = tools
        self.backstory = backstory
        self.verbose = verbose

    def perform_task(self, task):
        # Implement the logic to perform the task here
        pass