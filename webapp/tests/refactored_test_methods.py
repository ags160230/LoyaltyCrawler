import os
import shutil
import sys
# Refactored actions that are common between test cases

# Create a text file called t.txt, inside the folder that initiated this python session, nested inside a folder called /tmp
# Return a string path to a second directory, in the folder that initiated this python session, nexted inside a folder called /tmp2
def create_t_txt_in_tmp_dir():
    system_paths = sys.path
    # item at index 1 in system_paths is the folder that initiated the python interpreter
    current_dir = system_paths[1]
    temp_dir = current_dir + os.sep + 'tmp'
    temp_dir_2 = current_dir + os.sep + 'tmp2'
    try:
	   # create directory if it does not exist
       os.mkdir(temp_dir)
    except OSError:
	   # Else Error is raised, do nothing and continue
       pass
    try:
	   # create directory if it does not exist
       os.mkdir(temp_dir_2)
    except OSError:
	   # Else Error is raised, do nothing and continue
       pass
    file_name = 't.txt'
    # begin test
    source_file =  temp_dir + os.sep + file_name
    # open blank file at source location
    f = open(source_file,"w+")
    # close blank file
    f.close()
    destination_dir = temp_dir_2
    return_list = [source_file, destination_dir]
    return return_list
   
# Remove both nested temp folders, tmp and tmp2
def delete_temp_dirs():
    system_paths = sys.path
    # item at index 1 in system_paths is the folder that initiated the python interpreter
    current_dir = system_paths[1]
    temp_dir = current_dir + os.sep + 'tmp'
    temp_dir_2 = current_dir + os.sep + 'tmp2'
    try:
	   # Delete directory if it exists
       shutil.rmtree(temp_dir)
    except Exception:
	   # Else Exception is raised, do nothing and continue
       pass
    try:
       # Delete directory if it exists
       shutil.rmtree(temp_dir_2)
    except Exception:
	   # Else Exception is raised, do nothing and continue
       pass