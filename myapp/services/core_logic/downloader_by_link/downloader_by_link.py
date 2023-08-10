import aiohttp
import pathlib
from myapp.services.core_logic.downloader_by_link.interface_dowloader_by_link import IDownloaderByLiknk
from myapp.services.core_logic.downloader_file.interface_downloader_file import IDownloaderFile




class DownloadByLink(IDownloaderByLiknk):

    def __init__(self, session:aiohttp.ClientSession, downloader : IDownloaderFile) -> None:
        self.session = session
        self.downloader = downloader

    
    async def _create_get_request(self,url: str) -> aiohttp.ClientResponse:
        out_response = await self.session.get(url)
        return out_response
    
    
    async def download(self, url: str,path:pathlib.Path) -> None:

        response = await self._create_get_request(url)
        path_to_download = path

        async with response:
            await self.downloader.download_file(response,path_to_download)






