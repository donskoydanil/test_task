import os
import pytest




def test_create_directory(directory_for_tests,create_path):

    dir_exist = os.path.exists(create_path)
    assert dir_exist == True , "this path doesn't exist."


@pytest.mark.parametrize('parts_of_path',
                         [
                             ['test_dir','inner']
                         ] )
def test_directory_creation_not_existing_directory_error(
        directory_for_tests,
        parts_of_path,
        instance_directory_creator
):

    exist_error = False

    try:
        instance_directory_creator.create_direcory(parts_of_path)
    except FileExistsError:
        exist_error = True 

    assert exist_error == False
        


