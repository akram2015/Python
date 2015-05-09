# this program Prompt user to enter a start path and file name, then search recursively for the given file name starting at the given path,
# when file is found, it display the full path to the file

import os
import fnmatch
found = True
start_dir = input ("Enter the path: ")
file_name = input ("Enter file name: ")
for dirpath, dirs, files in os.walk(start_dir): # walk in path 
    for single_file in files:
        if fnmatch.fnmatch(single_file, file_name):     # check if the file is match
            print (os.path.join(dirpath, file_name))    # print the joining of directory path and the file
            found = False
if found:
    print ("The file is not exist in this path!")
        
