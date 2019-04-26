from django.test import TestCase
from folder_operations import *
from tests.refactored_test_methods import *

# Start of Test Cases

# perform setup tasks for all Tests in this file
def test_set_folder_environment():
    print("Setup")
	   
def test_get_folder_tree():
    current_folder = get_current_folder()
    get_folder_tree(current_folder)


# perform cleanup tasks after Test case completion
# ensures conscientious cleanup
def test_cleanup():
    print("Clean up")
