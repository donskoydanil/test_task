import aiohttp
import aiofiles
import pathlib
from typing import Type
from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.infrastructure.files_interfaces.status_interface.file_status_interface import FileStatusInterface
from myapp.services.core_logic.download.base_download import IDownloader



class DownloadWithProcents(IDownloader):

    def __init__(self, 
                 saver_of_procents:Type[FileProgressInterface],
                 status_changer:Type[FileStatusInterface]
                 ) -> None:
        self.saver_of_procents = saver_of_procents
        self.status_changer = status_changer
        


    def _count_size_of_response_answer(self,response:aiohttp.ClientResponse) -> int:
        size = int(response.headers['Content-Length'])
        return size
    
    def _save_procents(self, procents:int) -> None:
        self.saver_of_procents.change_progress(procents)

    def _change_status(self):
        self.status_changer.change_status()


    async def download(self, response:aiohttp.ClientResponse, path:pathlib.Path) -> None:
        self._change_status()
        size_of_answer = self._count_size_of_response_answer(response)
        progress = 0
        async with aiofiles.open(path, 'wb') as file:
            async for data in response.content.iter_any():
                await file.write(data)
                progress += len(data)
                calculated_procent = (progress / size_of_answer) * 100
                procent_of_download = int(calculated_procent)
                self._save_procents(procent_of_download)