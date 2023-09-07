import abc
from typing import Iterable


class IDirectoryCreator(abc.ABC):

    @abc.abstractmethod
    def create_direcory(self, parts_of_path: Iterable[str]) -> None:
        return NotImplemented
    



class IDirectoryDeleter(abc.ABC):

    @abc.abstractmethod
    def delete_direcory(self, parts_of_path: Iterable[str]) -> None:
        return NotImplemented