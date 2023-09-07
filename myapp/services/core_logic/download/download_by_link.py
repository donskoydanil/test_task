import aiohttp
import pathlib
from myapp.services.core_logic.download.base_download import IDownloader
from myapp.services.core_logic.download.download_with_procents import DownloadWithProcents



class DownloadByLink(IDownloader):

    def __init__(self, session:aiohttp.ClientSession, downloader : IDownloader) -> None:
        self.session = session
        self.downloader = downloader

    
    async def _create_get_request(self,url: str) -> aiohttp.ClientResponse:
        out_response = await self.session.get(url)
        return out_response
    
    
    async def download(self, url: str,path:pathlib.Path) -> None:

        response = await self._create_get_request(url)
        path_to_download = path

        async with response:
            await self.downloader.download(response,path_to_download)