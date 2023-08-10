from typing import Type,Optional
from myapp.infrastructure.container_interfaces.get_interface.container_get_interface import ContainerGetInterface
from myapp.domain.files.file import File

class FileBaseInterface:

    def __init__(self, id: str, 
                 container_get_interface: Optional[Type[ContainerGetInterface]] = None
                 ) -> None:
        
        if container_get_interface is None:
            container_get_interface = ContainerGetInterface()

        self.file_instance = self._get_file_instance(id,container_get_interface)


    def _get_file_instance(self,id: str, 
                 container_get_interface: Type[ContainerGetInterface]
                 ) -> Type[File] :
        return container_get_interface.get(id)



        