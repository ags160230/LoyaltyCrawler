from django.test import TestCase
from file_operations import *
from refactored_test_methods import *
import os
import shutil
import sys

# Start of Test Cases

# perform setup tasks for all Tests in this file
# ensure all old files are deleted before starting Test
def test_set_directory_environment():
	# Delete directories if they exist
    delete_temp_dirs()
	   
def test_move():
    returned_list = create_t_txt_in_tmp_dir()
    source = returned_list[0]
    destination = returned_list[1]
    shutil.move(source, destination)
    delete_temp_dirs()

def test_copy():
    returned_list = create_t_txt_in_tmp_dir()
    source = returned_list[0]
    destination = returned_list[1]
    copy_file(source, destination)
    delete_temp_dirs()

# perform cleanup tasks after Test case completion
# ensures conscientious cleanup
def test_cleanup():
	# Delete directories if they exist
    delete_temp_dirs()
