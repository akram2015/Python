# this program Prompt user for a file name, and read the file, then find and report if file contains a string with a string ("password=") in it.
# file name = read_it.txt

found = True
userinput = input ("Enter the file name: ")
string = input ("Enter the string: ")
myfile = open (userinput)  # open the file that might contain a string
for line in myfile:
    if string in line:
        print ("The line which contain the string", string, "is: ", line) # print the line that contain the string
        found = False
myfile.close()
if found:
        print ("The string", string, "does not exist in", userinput, "file!")
        

