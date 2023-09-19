from typing import Type
from myapp.infrastructure.tasks.task_container import TasksContainer


class BaseInterface:
    def __init__(self, task_container:Type[TasksContainer]) -> None:
        self.task_container = task_container