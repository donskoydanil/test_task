from typing import Self


class Container:

    _instance = None

    def __new__(cls,*args,**kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__memory = {}
        return cls._instance

    @property
    def memory(self):
        return self.__memory
    