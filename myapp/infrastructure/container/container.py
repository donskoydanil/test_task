from typing import Self, Dict,Type
from myapp.domain.files.file import File


class Container:

    _instance = None

    def __new__(cls,*args,**kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__memory = {}
        return cls._instance

    @property
    def memory(self) -> Dict[str,Type[File]]:
        return self.__memory
    