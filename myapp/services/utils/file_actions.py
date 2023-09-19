from typing import Callable,Type,Iterable
from myapp.domain.files.file import File
from functools import partial
from myapp.services.utils.create import create_directory
from myapp.services.utils.create import create_empty_file
from myapp.services.utils.container_actions import add_file_in_container
from myapp.infrastructure.container_interfaces.get_interface.container_get_interface import ContainerGetInterface


def prepare_file_before_actions(
        id:str,
        creator_directory:Callable[[Iterable[str]],None],
        creator_empty_file:Callable[[],Type[File]],
        add_file_in_memory:Callable[[str,Type[File]],None],

) -> None:
    
    creator_directory(id)
    empty_file = creator_empty_file()
    add_file_in_memory(id,empty_file)



def get_file_out_info(
        id: str,
        container_get_interface: Type[ContainerGetInterface]
)->str:
    file = container_get_interface.get(id)
    file_info = file.out_info
    return file_info







prepare_file = partial(
    prepare_file_before_actions,
    creator_directory = create_directory,
    creator_empty_file = create_empty_file,
    add_file_in_memory = add_file_in_container
    
)

get_file_info = partial(
    get_file_out_info,
    container_get_interface = ContainerGetInterface()

)









    