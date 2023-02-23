import os, sys
from os.path import abspath, dirname, join

## its application
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

# from course import course_details  ## there is a need to collapse the folder paths done above

def pay():
    print("This is my first payment function")

# print("function imported from course_detials, inside course folder: ")

# course_details.cfun()