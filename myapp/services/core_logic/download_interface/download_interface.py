import pathlib
from typing import Type
from myapp.services.core_logic.downloader_by_link.downloader_by_link import DownloadByLink
from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface
from myapp.services.core_logic.downloader_file.downloader_file_with_procents import DownloadFileWithProcents

class DownloadInterafce:

    def __init__(self,
                download_link_instace:Type[
                    DownloadByLink[ClientSessionInterface,DownloadFileWithProcents]
                    ]
                ) -> None:
        self.download_link_instace = download_link_instace
    
    async def download(self, url:str, path:pathlib.Path):
        await self.download_link_instace.download(url,path)