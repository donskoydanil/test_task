import abc 
from typing import Iterable,Optional





class IPathManager(abc.ABC):

    
    @abc.abstractmethod
    def construct_path_from_parts(self, parts_of_path:Iterable[str]) -> str:
        raise NotImplemented

