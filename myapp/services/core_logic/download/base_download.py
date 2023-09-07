import abc
import aiohttp
import pathlib


class IDownloader(abc.ABC):

    @abc.abstractmethod
    def download(self,response:aiohttp.ClientResponse, path:pathlib.Path) -> None:
        raise NotImplementedError