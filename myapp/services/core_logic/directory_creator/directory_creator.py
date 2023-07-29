import pathlib
from typing import Iterable
from myapp.services.core_logic.directory_creator.interface_directory_creator import IDirectoryCreator
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager 


class DirectoryCreator(IDirectoryCreator):

    def __init__(self,path_manager : IPathManager ) -> None:
        self.path_manager = path_manager
        
    def _check_path_exist(self,path: pathlib.PurePosixPath) -> bool:
        return self.path_manager.path_exists(path)
    
    def create_direcory(self, parts_of_path: Iterable[str]) -> None:
        
        direcory_to_create = self.path_manager.construct_path_from_parts(parts_of_path)

        if not self._check_path_exist(direcory_to_create):
             direcory_to_create.mkdir()
        




        

