from django.test import TestCase
from file_operations import *
from tests.refactored_test_methods import *

# Start of Test Cases

# perform setup tasks for all Tests in this file
# ensure all old files are deleted before starting Test
def test_set_folder_environment():
	# Delete directories if they exist
    delete_temp_folders()
	   
def test_move():
    returned_list = create_t_txt_in_tmp_folder()
    source = returned_list[0]
    destination = returned_list[1]
    move_file(source, destination)
    delete_temp_folders()

def test_copy():
    returned_list = create_t_txt_in_tmp_folder()
    source = returned_list[0]
    destination = returned_list[1]
    copy_file(source, destination)
    delete_temp_folders()

# perform cleanup tasks after Test case completion
# ensures conscientious cleanup
def test_cleanup():
	# Delete directories if they exist
    delete_temp_folders()
