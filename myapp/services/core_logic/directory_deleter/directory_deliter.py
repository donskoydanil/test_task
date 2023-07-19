import os
import shutil
from typing import Iterable
from interface_directory_deliter import IDirectoryDeliter
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager 


class DirectoryDeleter(IDirectoryDeliter):

    def __init__(self,path_manager : IPathManager ) -> None:
        self.path_manager = path_manager
        


    def delete_direcory(self, parts_of_path: Iterable[str]) -> None:
        
        direcory_to_delete = self.path_manager.construct_path_from_parts(parts_of_path)

        if os.path.exists(direcory_to_delete):
            shutil.rmtree(direcory_to_delete)