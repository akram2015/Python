# Akram Hussein

from random import randrange # to generate random number

print ("INTEGER DIVISIONS")
while True:
    a = randrange(5)  # random number(0-5)
    b = randrange(20) # random number(0-20)
    try:
        result = b//a  # for integer division
        answer = input(str (b) + "/" + str (a) + "= ")
        if result == int(answer):
            print ("CORRECT!\n")   
        else:
            print ("INCORRECT!\n")
    except ZeroDivisionError:    # exception for zero division
        print (b,"/",a,"=") 
        print ("division by zero\n")
    except ValueError:           # exception for non integer input
        print ("Please enter Integers Only!\n")
