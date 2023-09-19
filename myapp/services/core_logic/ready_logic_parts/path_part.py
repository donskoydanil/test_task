import pathlib
from typing import Type
from pydantic import BaseModel, computed_field
from myapp.settings.services_settings import ARCHIVES_DIRECTORY
from myapp.services.core_logic.pathmanager.interface_path_manager import IPathManager
from myapp.services.core_logic.pathmanager.path_manager import PathManager


class PathManagerArchive(BaseModel):
    start_path : Type[pathlib.Path] = ARCHIVES_DIRECTORY

    @computed_field(return_type=Type[IPathManager])
    @property
    def get_ready_instance(self):
        return PathManager(self.start_path)
    


def get_ready_path_manager(
        interface_maker:Type[PathManagerArchive] = PathManagerArchive()
        ) ->IPathManager:
    ready_ready_instance = interface_maker.get_ready_instance
    return ready_ready_instance