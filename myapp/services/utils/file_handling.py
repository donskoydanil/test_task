from typing import Callable
from myapp.services.core_logic.ready_logic_parts.download_part import get_ready_download_instance
from myapp.services.core_logic.download.base_download import IDownloader

async def download_and_unpacking(
        id: str, 
        url: str, 
        path: str, 
        downloader_maker:Callable[[str],IDownloader] = get_ready_download_instance
)-> None:
    downloader = downloader_maker(id)
    await  downloader.download(url,path)