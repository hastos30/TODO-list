from task import Task
import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title_task):
        task = Task(self.next_id, title_task)
        self.tasks.append(task)
        self.next_id += 1

    def show_tasks(self):
        if not self.tasks:
            print("Задач нет")
        else:
            for task in self.tasks:
                print(f"\n{task}")
    
    def search_task(self, text):
        result = []

        for task in self.tasks:
            if text.lower() in task.title.lower():
                result.append(task)

        return result
    
    def find_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        
        return None
    
    def remove_task(self, task_id):
        task = self.find_by_id(task_id)

        if task is None:
            return False
        
        self.tasks.remove(task)
        return True
                

    def rename_task(self, task_id, title):
        task = self.find_by_id(task_id)

        if task is None:
            return False
        task.rename(title)
        return True
    
    def save_txt(self, filename):
        with open(f'src/save/{filename}.txt', 'w', encoding="utf-8") as file:
            for task in self.tasks:
                file.write(f"{task.id};{task.title}\n")
    
    
    def load_txt(self, filename):
        try:
            with open(f'src/save/{filename}.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    
                    if not line:
                        continue

                    task_id, title = line.split(';', maxsplit=1)
                    task = Task(int(task_id), title)
                    self.tasks.append(task)

            if self.tasks:
                self.next_id = max(task.id for task in self.tasks) + 1
            else:
                self.next_id = 1
        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1


        

