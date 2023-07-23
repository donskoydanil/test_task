import abc 
import pathlib
from typing import Iterable,Optional





class IPathManager(abc.ABC):

    @abc.abstractmethod
    def path_exists(self, path: pathlib.PurePosixPath) -> bool:
       raise NotImplemented
    
    @abc.abstractmethod
    def construct_path_from_parts(self, parts_of_path:Iterable[str]) -> str:
        raise NotImplemented

