import abc
from typing import Iterable


class IDirectoryDeleter(abc.ABC):

    @abc.abstractmethod
    def delete_direcory(self, parts_of_path: Iterable[str]) -> None:
        return NotImplemented