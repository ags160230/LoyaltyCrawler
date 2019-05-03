import shutil
import os

# link describing os functions
# https://docs.python.org/2/library/os.html

# link describing shutil functions used below
#https://docs.python.org/2/library/shutil.html

# Function to copy a file from a source location to a destination location
def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        return True
    except FileExistsError:
        # display error message
        return False
    
# Function to move a file from a source location to a destination location	
def move_file(src, dst):
    try:
        shutil.move(src, dst)
        return True
    except FileExistsError:
        # display error message
        return False
		

# Function to delete a file from a source location
def delete_file(src):
    try:
        os.remove(src)
        return True
    except OSError:
         # display error message
        return False
    
	
# Function to rename a file from a source location to a destination location	
def rename_file(src, dest):
    try:
        os.rename(src, dest)
        return True
    except OSError:
         # display error message
        return False
   	
	
