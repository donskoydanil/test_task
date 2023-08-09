import aiohttp
import aiofiles
import pathlib
from typing import Type
from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.services.core_logic.downloader_file.interface_downloader_file import IDownloaderFile



class DownloadFileWithProcents(IDownloaderFile):

    def __init__(self, saver_of_procents:Type[FileProgressInterface]) -> None:
        self.saver_of_procents = saver_of_procents


    def _count_size_of_response_answer(self,response:aiohttp.ClientResponse) -> int:
        size = int(response.headers['Content-Length'])
        return size
    
    def _save_procents(self, procents:int) -> None:
        self.saver_of_procents.change_progress(procents)


    async def download_file(self, response:aiohttp.ClientResponse, path:pathlib.Path) -> None:
        size_of_answer = self._count_size_of_response_answer(response)
        progress = 0
        async with aiofiles.open(path, 'wb') as file:
            async for data in response.content.iter_any():
                await file.write(data)
                progress += len(data)
                calculated_procent = (progress / size_of_answer) * 100
                procent_of_download = int(calculated_procent)
                self._save_procents(procent_of_download)





