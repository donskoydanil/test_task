import pathlib
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager
from myapp.settings.services_settings import BASE_DIRECTORY
from typing import Iterable,Optional





class PathManager(IPathManager):

    def __init__(self,base_dir:Optional[str] = None ) -> None:
        if base_dir is None:
            base_dir = BASE_DIRECTORY

        self.base_dir = base_dir
            
    def path_exists(self, path: pathlib.PurePosixPath) -> bool:
        return path.exists()


    def construct_path_from_parts(self,parts_of_path:Iterable[str]) -> pathlib.PurePosixPath:
        return self.base_dir.joinpath(*parts_of_path)



    
        
