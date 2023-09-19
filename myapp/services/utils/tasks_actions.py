import asyncio
from typing import Type
from functools import partial
from myapp.infrastructure.tasks.task_container import TasksContainer
from myapp.infrastructure.tasks.task_container_interfaces.get import GetTasksContainerInterface



async def close_tasks(
        task_list_get_interface:Type[GetTasksContainerInterface]
) -> None:

    task_list = task_list_get_interface.get_all_tasks()


    for task in task_list:

        exeception_flag = False
        
        try:

            async with asyncio.timeout(0.01):
                await task

        except Exception as exc:

            if type(exc) is not TimeoutError:
                print(f'catch exception in task with id - {task.get_name()}\n{exc}')
            else:
                exeception_flag = True

        
        if exeception_flag:

            task.cancel()

            try:
                await task 

            except asyncio.CancelledError:
                print(f'task with id - "{task.get_name()}" is closed')



close_tasks = partial(
    close_tasks,
    task_list_get_interface =  GetTasksContainerInterface(TasksContainer())
)