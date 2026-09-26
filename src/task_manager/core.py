from typing import Any
from enum import Enum
from dataclasses import dataclass, field
from datetime import date
from typing import Callable

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    due_date: date | None = None # Olabilirde olmayabilirde
    tags: list[str] = field(default_factory=list) # Her seferinde bellekte yeni bir liste açar aynı listeyi kullanmaz ve bir instance
    priority: Priority = Priority.MEDIUM 

class TaskNotFoundError(Exception):
    pass
  
def sort_tasks(tasks: list[Task], key:Callable[[Task], Any]) -> list[Task]:
    return sorted(tasks, key=key)

def search_tasks(tasks:list[Task], key:Callable[[Task], Any]) -> list[Task]:
    return [task for task in tasks if key(task)]

class TaskManager:
    def __init__(self) -> None:
        self.tasks: dict[int,Task] = {}
        self.next_id: int = 1
    
    def get_task(self, task_id:int) -> Task | None:
        return self.tasks.get(task_id)

    def complete_task(self, task_id:int) -> None:
        if task_id not in self.tasks:
            raise TaskNotFoundError(f"Task ID '{task_id}' not found")
        self.tasks[task_id].done = True
    
    def add_task(self, title:str, due:date | None = None) -> Task:
        task = Task(id=self.next_id, title=title, due_date=due)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    def list_tasks(self, filter_done : bool | None = None) -> list[Task]:
        if filter_done is None:
            return list(self.tasks.values())
        if filter_done is True:
            return [task for task in self.tasks.values() if task.done is True]
        else:
            return [task for task in self.tasks.values() if task.done is False]

        
