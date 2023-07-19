import os
from typing import Iterable
from interface_directory_creator import IDirectoryCreator
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager 


class DirectoryCreator(IDirectoryCreator):

    def __init__(self,path_manager : IPathManager ) -> None:
        self.path_manager = path_manager
        


    def create_direcory(self, parts_of_path: Iterable[str]) -> None:
        
        direcory_to_create = self.path_manager.construct_path_from_parts(parts_of_path)

        if not os.path.exists(direcory_to_create):
             os.makedirs(direcory_to_create)
        




        
