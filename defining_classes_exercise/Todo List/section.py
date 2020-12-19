from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in [x for x in self.tasks]:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        all_tasks = [x.name for x in self.tasks]
        if task_name in all_tasks:
            task = self.tasks[all_tasks.index(task_name)]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed = [c for c in self.tasks if c.completed == False]
        result = len(self.tasks) - len(completed)
        for x in completed:
            if x in self.tasks:
                self.tasks.remove(x)
        return f"Cleared {result} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        result += '\n'.join([f'{x.details()}' for x in self.tasks])
        return result
