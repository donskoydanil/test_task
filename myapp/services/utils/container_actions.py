from typing import Type
from myapp.domain.files.file import File
from myapp.infrastructure.container_interfaces.add_interface.container_add_interface import ContainerAddInterface



def add_file_in_container(
        id:str,
        file_to_add:Type[File],
        interface :Type[ContainerAddInterface] = ContainerAddInterface()
) -> None:
    
    interface.add(id,file_to_add)
