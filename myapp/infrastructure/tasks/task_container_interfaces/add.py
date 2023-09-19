from typing import Awaitable
from myapp.infrastructure.tasks.task_container_interfaces.base import BaseInterface




class AddTasksContainerInterface(BaseInterface):

    async def add(self, task:Awaitable) -> None:
        task_list = self.task_container.get_tasks
        task_list.append(task)