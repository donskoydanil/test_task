import abc
import aiohttp
import pathlib


class IDownloaderFile(abc.ABC):

    @abc.abstractmethod
    def download_file(self,response:aiohttp.ClientResponse, path:pathlib.Path) -> None:
        raise NotImplementedError