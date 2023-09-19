from typing import Optional, Type
from myapp.infrastructure.container_interfaces.get_interface.container_get_interface import ContainerGetInterface
from myapp.infrastructure.files_interfaces.base_interface.file_base_interface import FileBaseInterface

class FileStatusInterface(FileBaseInterface):

    def __init__(self, 
                 id: str, 
                 status:str, 
                 container_get_interface: type[ContainerGetInterface] | None = None
                 ) -> None:
        super().__init__(id, container_get_interface)
        self.status = status

    def change_status(self) -> None:
        self.file_instance.status = self.status