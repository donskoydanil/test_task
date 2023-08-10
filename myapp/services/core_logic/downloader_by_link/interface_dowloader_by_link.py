import abc
import aiohttp
import pathlib



class IDownloaderByLiknk(abc.ABC):

    @abc.abstractmethod
    def _create_get_request(self, url:str) -> aiohttp.ClientResponse:
        raise NotImplementedError
    
    @abc.abstractmethod
    def download(self, url:str, path:pathlib.Path) -> None:
        raise NotImplementedError
    
    

