import pathlib
from myapp.services.core_logic.downloader_by_link.interface_dowloader_by_link import IDownloaderByLiknk
class DownloadInterafce:

    def __init__(self, download_link_instace:IDownloaderByLiknk) -> None:
        self.download_link_instace = download_link_instace
    
    async def download(self, url:str, path:pathlib.Path):
        await self.download_link_instace.download(url,path)