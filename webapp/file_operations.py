import shutil
import os

# Function to copy a file from a source location to a destination location
def copy_file(source, dest):
    try:
        shutil.copy2(source, dest)
        return True
    except FileExistsError:
        # display error message
        return False
    
# Function to move a file from a source location to a destination location	
def move_file(source, dest):
    try:
        shutil.move(source, dest)
        return True
    except FileExistsError:
        # display error message
        return False

	
	
