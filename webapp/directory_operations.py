import os
import shutil

# link describing os functions
# https://docs.python.org/2/library/os.html

# link describing shutil functions used below
#https://docs.python.org/2/library/shutil.html

# Function to create a directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        return True
    except FileExistsError:
        # display error message
        return False

# Function to copy a directory to a destination location
def copy_directory(src, dst):
    try:
        shutil.copytree(src, dst, symlinks=True, ignore=None)
        return True
    except OSError:
        # display error message
        return False

# Function to delete a directory
def delete_directory(path):
    try:
        shutil.rmtree(path)
        return True
    except OSError:
         # display error message
        return False
	   
# Function to move a directory to a destination location  
def move_directory(src, dest):
   try:
        move(src, dst)
        return True
   except OSError:
        # display error message
        return False

