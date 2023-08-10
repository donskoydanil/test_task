from typing import Any


class FileBaseDescriptor:

    
    def __set_name__(self, owner,name:str) -> None:
        self.name = '_' + name

    def __get__(self,instance,owner) -> Any:
        return instance.__dict__[self.name]
    
    def __set__(self,instance, value:Any) -> None:
        instance.__dict__[self.name] = value