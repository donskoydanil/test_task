
import pytest
from myapp.settings.services_settings import BASE_DIRECTORY,ARCHIVES_DIRECTORY
from myapp.services.core_logic.pathmanager.path_manager import PathManager




@pytest.mark.parametrize('path_manager, base_directory',
                         [
                             (PathManager,BASE_DIRECTORY)
                         ] )
def test_empty_base_dir_initialization(path_manager,base_directory):
    path_manger_class = path_manager()
    assert path_manger_class.base_dir == base_directory


@pytest.mark.parametrize('another_directory, path_manager',
                         [
                             (ARCHIVES_DIRECTORY,PathManager)
                         ] )
def test_base_dir_initialization(another_directory,path_manager):
    path_manger_class = path_manager(another_directory)
    assert path_manger_class.base_dir == another_directory

@pytest.mark.parametrize('path_manager, base_directory',
                         [
                             (PathManager(),BASE_DIRECTORY)
                        ])
def test_empty_list_with_parts_path(path_manager,base_directory):
    empty_list_with_parts = []
    out_for_assert = path_manager.construct_path_from_parts(empty_list_with_parts) 
    assert out_for_assert == base_directory


@pytest.mark.parametrize('path_manager, base_directory,lists_with_parts',
                         [
                             (PathManager(),BASE_DIRECTORY,['archive','test_1'])
                        ])
def test_construct_pathes(path_manager,base_directory,lists_with_parts):

    path_to_check = base_directory.joinpath(*lists_with_parts)
    path_pm_construct_path= path_manager.construct_path_from_parts(lists_with_parts) 
    assert path_to_check == path_pm_construct_path
    

    






