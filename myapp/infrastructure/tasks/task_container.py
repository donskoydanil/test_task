from typing import Awaitable,List


class TasksContainer:

    _instance  = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._tasks = []
        return cls._instance
    
    @property
    def get_tasks(self)->List[Awaitable]:
        return self._tasks
    