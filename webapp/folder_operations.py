import os
import shutil

# link describing os functions
# https://docs.python.org/2/library/os.html

# link describing shutil functions used below
#https://docs.python.org/2/library/shutil.html

# Function to create a directory
def create_folder(directory_name):
    try:
        os.mkdir(directory_name)
        return True
    except FileExistsError:
        # display error message
        return False

# Function to copy a directory to a destination location
def copy_folder(src, dst):
    try:
        shutil.copytree(src, dst, symlinks=True, ignore=None)
        return True
    except OSError:
        # display error message
        return False

# Function to delete a directory
def delete_folder(path):
    try:
        shutil.rmtree(path)
        return True
    except OSError:
         # display error message
        return False
	   
# Function to move a directory to a destination location  
def move_folder(src, dest):
   try:
        move(src, dst)
        return True
   except OSError:
        # display error message
        return False

# Function to return file tree
def get_folder_tree (start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))