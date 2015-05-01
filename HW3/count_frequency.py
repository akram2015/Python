# this function takes a list of words as an argument, counts how many times each word appears in the list,
# and then returns this frequency listing as a Python dictionary

#from collections import Counter     # import counter module
def count_frequency():
    mylist = input( "Enter your list separated by spaces: ")  # prompt user to enter words 
    split_list = mylist.split()                               # split words into list
    # counting how many times each word appears in the list, then convert them into dictionary
    my_dictionary = dict([(word, split_list.count(word)) for word in (split_list)])  
    # counts = Counter(split_list)   # convert to dictionary using 
    print(my_dictionary)
count_frequency()
