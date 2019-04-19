from django.test import TestCase
from file_operations import *
import os
import shutil


# Create your tests here.
def test_move():
   source = os.path.join('C:', os.sep, 'Users', 'Alex', 't.txt')
   # open blank file at source location
   f= open(source,"w+")
   # close blank file
   f.close()
   destination = os.path.join('C:', os.sep, 'Users', 'Alex', 'Desktop', 't.txt')
   shutil.move(source, destination)

def test_copy():
   source = os.path.join('C:', os.sep, 'Users', 'Alex', 't.txt')
   # open blank file at source location
   f= open(source,"w+")
   # close blank file
   f.close()
   destination = os.path.join('C:', os.sep, 'Users', 'Alex', 'Desktop', 't.txt')
   copy_file(source, destination)
