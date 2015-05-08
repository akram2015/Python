# This program shows the execution time for a same operation first by using dictionary, second by using shelve.
# by comparing the execution time for both we see the dictionary is faster because it excute the code in RAM and print the result from RAM,
# while shelve execute the code and write to the disk then to read the shelve file, it takes more time to read from the disk and print the result.

from datetime import datetime  # to calculate time
import shelve

# for dictionary
dt1 = datetime.now()
myinfo = {1:"my name is Frank", 2:"Im 25 years old", 3:"Im living in US"}
for item in myinfo:
    print (myinfo[item]) # print the dictionary
dt2 = datetime.now()
print ("Excution time for dictionary is: ", dt2.microsecond-dt1.microsecond,"\n")

# for shelve
dt3 = datetime.now()
s = shelve.open("myinfo.txt")   # creat file for write
s["myinfo.txt"] = {1:"my name is Frank", 2:"Im 25 years old", 3:"Im living in US"} # write to the file
s.close()
s = shelve.open("myinfo.txt")   # open file to read
info = s["myinfo.txt"]          # read from file
for item in info:
    print (info[item])
dt4 = datetime.now()
print ("Excution time for shelve is: ", dt4.microsecond-dt3.microsecond)
