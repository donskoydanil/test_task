from typing import Type
from myapp.domain.files.file import File
from myapp.infrastructure.container_interfaces.base_interface.base_container_interface import ContainerBaseInterface


class ContainerGetInterface(ContainerBaseInterface):

    def get(self,id:str) -> Type[File]:
        return self.container.memory[id]
