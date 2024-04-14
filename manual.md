# Phosphorus Agent System User Manual

## Introduction

The Phosphorus Agent System is an AI agent workflow built using the Multi Agent Framework CREW.AI. It allows you to create and manage agents with specific roles to complete tasks assigned to them. This user manual provides detailed instructions on how to install and use the Phosphorus Agent System.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Creating Agents](#creating-agents)
   - [Assigning Tasks](#assigning-tasks)
   - [Running the Workflow](#running-the-workflow)
3. [Conclusion](#conclusion)

## Installation <a name="installation"></a>

To install the Phosphorus Agent System, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the Phosphorus Agent System repository from GitHub:

   ```
   git clone https://github.com/your-username/phosphorus-agent-system.git
   ```

3. Navigate to the cloned repository:

   ```
   cd phosphorus-agent-system
   ```

4. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

5. You have successfully installed the Phosphorus Agent System.

## Usage <a name="usage"></a>

### Creating Agents <a name="creating-agents"></a>

To create a new agent, you can use the `create_agent` function in the `main.py` file. This function takes two parameters: `agent_name` and `agent_role`. Here's an example:

```python
agent1 = create_agent("Agent1", "Role1")
```

This will create a new agent with the name "Agent1" and the role "Role1". You can create as many agents as you need.

### Assigning Tasks <a name="assigning-tasks"></a>

To assign a task to an agent, you can use the `assign_task` function in the `main.py` file. This function takes two parameters: `agent` and `task`. Here's an example:

```python
assign_task(agent1, "Task1")
```

This will assign the task "Task1" to the agent `agent1`. You can assign tasks to multiple agents.

### Running the Workflow <a name="running-the-workflow"></a>

To run the workflow and execute the tasks assigned to the agents, you can use the `run` method of the `Workflow` class in the `main.py` file. Here's an example:

```python
workflow.run()
```

This will run the workflow and display the execution status of each agent and their assigned tasks.

## Conclusion <a name="conclusion"></a>

Congratulations! You have successfully installed and learned how to use the Phosphorus Agent System. You can now create agents, assign tasks, and run the workflow to manage your AI agent system. If you have any further questions or need assistance, please refer to the documentation or contact our support team.

Happy agent managing!