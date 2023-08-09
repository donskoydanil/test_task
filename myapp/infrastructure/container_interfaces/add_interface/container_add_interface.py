from myapp.infrastructure.container.container import Container
from myapp.domain.files.file import File
from typing import Type



class ContainerAddInterface:

    def __init__(self, container:Type[Container]) -> None:
        if container is None:
            container = Container()

        self.container = container

    def add(self,id:str,file:Type[File]) -> None:
        self.container.memory[id] = file