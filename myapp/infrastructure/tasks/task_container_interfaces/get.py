from typing import Type,List,Awaitable
from myapp.infrastructure.tasks.task_container_interfaces.base import BaseInterface



class GetTasksContainerInterface(BaseInterface):

    def get_all_tasks(self) -> List[Awaitable]:
        return self.task_container.get_tasks