import json
from datetime import datetime

class TaskManager:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, deadline, priority):
        task = {
            "description": description,
            "deadline": deadline,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, completed=False):
        tasks_to_list = [t for t in self.tasks if t['completed'] == completed]
        for i, task in enumerate(tasks_to_list, 1):
            print(f"{i}. {task['description']} | Prazo: {task['deadline']} | Prioridade: {task['priority']}")

    def complete_task(self, task_index):
        try:
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
        except IndexError:
            print("Tarefa inválida!")

    def remove_task(self, task_index):
        try:
            del self.tasks[task_index]
            self.save_tasks()
        except IndexError:
            print("Tarefa inválida!")

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [t for t in self.tasks if t['priority'].lower() == priority.lower() and not t['completed']]
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task['description']} | Prazo: {task['deadline']} | Prioridade: {task['priority']}")