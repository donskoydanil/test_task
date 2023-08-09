from myapp.infrastructure.container.container import Container
from myapp.infrastructure.container_interfaces.base_interface.base_container_interface import ContainerBaseInterface
from myapp.domain.files.file import File
from typing import Type



class ContainerAddInterface(ContainerBaseInterface):

    def add(self,id:str,file:Type[File]) -> None:
        self.container.memory[id] = file