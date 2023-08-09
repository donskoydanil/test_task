from typing import Type,Optional
from myapp.infrastructure.container_interfaces.get_interface.container_get_interface import ContainerGetInterface


class FileBaseInterface:

    def __init__(self, id: str, 
                 container_get_interface: Optional[Type[ContainerGetInterface]]
                 ) -> None:
        
        if container_get_interface is None:
            container_get_interface = ContainerGetInterface()

        self.get_interface = container_get_interface
        self.id = id

        