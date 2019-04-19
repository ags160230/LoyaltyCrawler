import shutil
import os

# Function to create a directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        return True
    except FileExistsError:
        # display error message
        return False

# Function to copy a directory to a destination location
def copy_directory(source, dest):
   try:
       shutil.copytree(src, dst, symlinks=False, ignore=None)
       return True
   except
        # display error message
       return False

# Function to move a directory to a destination location  
def move_directory(source, dest):
   try:
       shutil.copytree(src, dst, symlinks=False, ignore=None)
       return True
   except
        # display error message
       return False

# Function to delete a directory
def delete_directory(source):
   try:
       shutil.copytree(src, dst, symlinks=False, ignore=None)
       return True
   except
        # display error message
       return False