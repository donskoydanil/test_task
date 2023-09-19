from myapp.handlers.post import PostHandler
from myapp.services.service_layer.post_logic import ServicePost
from myapp.services.core_logic.ready_logic_parts.give_id_part import get_ready_giver_id
from myapp.services.utils.file_actions import prepare_file
from myapp.services.utils.create import create_path
from myapp.services.utils.create import create_url
from myapp.services.utils.file_handling import download_and_unpacking
from myapp.handlers.get import GetHandler
from myapp.services.service_layer.get_logic import ServiceGet
from myapp.services.utils.file_actions import get_file_info
from myapp.infrastructure.tasks.task_container import TasksContainer
from myapp.infrastructure.tasks.task_container_interfaces.add import AddTasksContainerInterface

def get_ready_post_handler():


    post_logic = ServicePost(
        get_ready_giver_id(),
        prepare_file,
        create_path,
        create_url,
        download_and_unpacking,
        AddTasksContainerInterface(TasksContainer())


    )


    post_handler = PostHandler(post_logic)

    return post_handler



def get_ready_get_handler():

    get_logic = ServiceGet(
        get_file_info
    )


    get_handler = GetHandler(get_logic)
    return get_handler



# post_logic = ServicePost(
#     get_ready_giver_id(),
#     prepare_file,
#     create_path,
#     create_url,
#     download_and_unpacking,
#     AddTasksContainerInterface(TasksContainer())


#     )


# import asyncio

# async def main():

#     await post_logic.start_service('AlmaLinux-8-amd64-5.57-202106301015.tar.gz')

#     from myapp.infrastructure.tasks.task_container import TasksContainer

#     t = TasksContainer()
#     for i in t.get_tasks:
#         print(i.get_name())
#         await i

# asyncio.run(main())