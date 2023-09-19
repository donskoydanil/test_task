import pathlib
import asyncio
from typing import Callable,Awaitable,Type, List
from myapp.services.core_logic.giver_id.giver_id import GiverId
from myapp.infrastructure.tasks.task_container_interfaces.add import AddTasksContainerInterface



class ServicePost:

    def __init__(
            self,
            giver_id : Type[GiverId],
            prepare_file : Callable[[],None],
            path_maker : Callable[[str], str],
            url_maker : Callable[[str], str],
            downloader_and_unpacker,
            task_add_interface : Type[AddTasksContainerInterface]
            # : Awaitable[List[str], None]
    ) -> None:
        self.giver_id = giver_id
        self.prepare_file = prepare_file
        self.path_maker = path_maker
        self.url_maker = url_maker
        self.downloader_and_unpacker = downloader_and_unpacker
        # self.task_add_interface = task_add_interface


    def _make_id(self) -> str:
        file_id = self.giver_id.give_id
        return file_id
    
    def _prepare_file(self, id : str) -> None:
        self.prepare_file(id)

    def _make_url(self, file_name : str) -> str:
        downlaod_url = self.url_maker(file_name)
        return downlaod_url

    def _make_path_to_file(self, id: str, file_name: str) ->pathlib.Path:
        return self.path_maker(id,file_name)
    
    async def _download_and_unpucking(
            self, 
            id: str,
            url: str,
            path: pathlib.Path
    ) -> None:
        await self.downloader_and_unpacker(id,url,path)
    
    async def start_service(self, file_name:str)->str:
        file_id = self._make_id()
        self._prepare_file(file_id)
        file_url = self._make_url(file_name)
        file_path = self._make_path_to_file(file_id, file_name)

        # service_task = asyncio.create_task(self._download_and_unpucking(
        #     file_id,
        #     file_url,
        #     file_path

        # ))

        asyncio.create_task(self._download_and_unpucking(
            file_id,
            file_url,
            file_path

        ))

        

        # await self.task_add_interface.add(service_task)

        

        return file_id