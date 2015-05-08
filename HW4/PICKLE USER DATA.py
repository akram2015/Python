# This program prompt user to enter Name, Age and Country of Origin, then uses Pickle to store it,
# then for a separate function the user can open the pickle and read it back.

import pickle
name = input ("Enter your name: ")
age = input ("Enter your age: ")
country = input ("Enter your country of origin: ")

f = open ("pickles.txt", "bw") # creat a file to write
mylist = [name, age, country]
pickle.dump(mylist, f)   # write to the file
f.close()                # close file

def read_pickle ():      # function
    f = open ("pickles.txt", "br")  # open the file to read
    mylist = pickle.load(f)         # read from file
    print (mylist)
    f.close()
read_pickle()            # call function
