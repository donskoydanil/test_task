import os
import shutil
from interface_path_manager import IPathManager
from myapp.settings.services_settings import BASE_DIRECTORY,ARCHIVES_DIRECTORY
from typing import Iterable,Optional





class PathManager(IPathManager):

    def __init__(self,base_dir:Optional[str] = None ) -> None:
        if base_dir is None:
            self.base_dir = BASE_DIRECTORY
            


    def construct_path_from_parts(self,parts_of_path:Iterable[str]) -> str:
        return os.path.join(self.base_dir, *parts_of_path)



    
        
