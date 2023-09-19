import pathlib
from typing import Type,Callable,Iterable
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager
from myapp.services.core_logic.ready_logic_parts.path_part import get_ready_path_manager
from myapp.services.core_logic.ready_logic_parts.directory_part import get_ready_directory_creator
from myapp.infrastructure.container_interfaces.get_interface.container_get_interface import ContainerGetInterface
from myapp.services.core_logic.directory_manilulations.base import IDirectoryCreator
from myapp.settings.services_dowload_settings import services_download_settings
from myapp.domain.files.file import File



def create_path(
        *parts_of_path:str,
        ready_path_manager:Callable[[],IPathManager] = get_ready_path_manager()
) -> pathlib.Path:
    
    out_path = ready_path_manager.construct_path_from_parts(parts_of_path)
    return out_path


def create_directory(
        *parts_of_path:str,
        ready_creator:Callable[[],IDirectoryCreator] = get_ready_directory_creator()
)-> None:
    ready_creator.create_direcory(parts_of_path)
    

def create_empty_file(
        progress:str = '',
        status:str = '',
        files:Iterable[str] = [''],
        file : Type[File] = File

) ->  Type[File]:
    
    out_file = file(progress,files,False,status)
    return out_file



# сделать специальный тип через тайпинг дляservices_download_settings
def create_url(
        file_name:str, 
        url_settings:Callable[[],str] = services_download_settings
)->str:
    start_url = url_settings.url

    final_url = start_url + file_name
    return final_url






    