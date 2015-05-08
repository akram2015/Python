# this program Prompt user to enter a start path and file name, then search recursively for the given file name starting at the given path,
# when file is found, it display the full path to the file

import os
import fnmatch

def check (start_dir,file_name): 
    for dirpath, dirs, files in os.walk(start_dir): # walk in path 
        for single_file in files:
            if fnmatch.fnmatch(single_file, file_name):
                return True                         # return true to the function if file in the path
            
start_dir = input ("Enter the path: ")
file_name = input ("Enter file name: ")
if check (start_dir,file_name):
    print (os.path.join(start_dir, file_name))      # join file to the path
else:
    print ("The file is not exist in this path!")
        
