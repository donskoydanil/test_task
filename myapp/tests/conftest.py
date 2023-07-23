import pytest 
from myapp.services.core_logic.directory_creator.directory_creator import DirectoryCreator
from myapp.services.core_logic.directory_deleter.directory_deliter import DirectoryDeleter
from myapp.services.core_logic.pathmanager.path_manager import PathManager
from myapp.settings.services_settings import BASE_DIRECTORY



@pytest.fixture()
def instance_path_manager():
    path_manager = PathManager(BASE_DIRECTORY)
    return path_manager

@pytest.fixture()
def instance_directory_creator(instance_path_manager):
    
    directory_creator = DirectoryCreator(instance_path_manager)
    return directory_creator

@pytest.fixture()
def instance_directory_deleter(instance_path_manager):
    directory_deleter = DirectoryDeleter(instance_path_manager)
    return directory_deleter




@pytest.fixture()
def create_path(instance_path_manager):

    path_to_construct = ['test_dir','inner']
    path_to_check = instance_path_manager.construct_path_from_parts(path_to_construct)
    return path_to_check

@pytest.fixture()
def directory_for_tests(instance_directory_creator,instance_directory_deleter):
    path_to_construct = ['test_dir','inner']
    instance_directory_creator.create_direcory(path_to_construct)

    yield

    instance_directory_deleter.delete_direcory(path_to_construct)





    

