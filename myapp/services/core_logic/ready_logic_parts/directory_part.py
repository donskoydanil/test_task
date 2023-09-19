from pydantic import BaseModel, computed_field
from typing import Type,Callable
from myapp.services.core_logic.directory_manilulations.create import DirectoryCreator
from myapp.services.core_logic.directory_manilulations.base import IDirectoryCreator
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager
from myapp.services.core_logic.ready_logic_parts.path_part import get_ready_path_manager



class DirectoryCreateInterface(BaseModel):

    path_manager : Callable[[],IPathManager] = get_ready_path_manager()

    @computed_field(return_type=Type[IDirectoryCreator])
    @property
    def get_ready_instance(self):
        return DirectoryCreator(self.path_manager)
    


def get_ready_directory_creator(
        interface_maker:Type[DirectoryCreateInterface] = DirectoryCreateInterface()
)->IDirectoryCreator:
    instance = interface_maker.get_ready_instance
    return instance
