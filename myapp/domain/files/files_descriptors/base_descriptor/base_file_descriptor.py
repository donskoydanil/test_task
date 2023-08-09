from typing import Type,Any
from myapp.domain.files.file import File

class FileBaseDescriptor:

    def __set_name__(self, owner:Type[File],name:str) -> None:
        self.name = '_' + name

    def __get__(self,instance:Type[File],owner:Type[File]) -> Any:
        return instance.__dict__[self.name]
    
    def __set__(self,instance:Type[File], value:Any) -> None:
        instance.__dict__[self.name] = value