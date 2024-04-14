'''
This file contains the Workflow class for managing the agent workflow.
'''
class Workflow:
    def __init__(self):
        self.tasks = []
        self.is_running = False
    def start_workflow(self):
        """
        Starts the workflow if it is not already running.
        """
        if not self.is_running:
            self.is_running = True
            print("Workflow started.")
        else:
            print("Workflow is already running.")
    def stop_workflow(self):
        """
        Stops the workflow if it is running.
        """
        if self.is_running:
            self.is_running = False
            print("Workflow stopped.")
        else:
            print("Workflow is not running.")
    def add_task(self, task):
        """
        Adds a task to the workflow if it doesn't already exist.
        """
        if task not in self.tasks:
            self.tasks.append(task)
            print(f"Task '{task}' added to the workflow.")
        else:
            print(f"Task '{task}' already exists in the workflow.")
    def remove_task(self, task):
        """
        Removes a task from the workflow if it exists.
        """
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the workflow.")
        else:
            print(f"Task '{task}' does not exist in the workflow.")