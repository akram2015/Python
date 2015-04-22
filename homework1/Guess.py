# This program for guesses an integer number between (1-100) that the user thought of. 
# then if the number is successfully guessed, will offer the user to play again
__author__ = 'akram'

name = input("whats your name? ")
print("hello " + name + "!" + " Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
play = True  
moreplay=True
while moreplay: # when the user wants to play more
    count = 1   # initialize the variables
    bottom = 1
    top = 100
    while play: # start game
        middle = (bottom + top)//2  # find a middle of numbers range
        answer = input("Is it "+ str(middle)+" ?(yes/no)")  # asking the user if the guess number is correct
        if answer == "yes":
            print("Yeey! I got it in", count, "trie!")
            break # go out the play while loop
        else:     # if the guess not correct
            compare = input("Is the number larger than "+ str(middle) + " ?(yes/no)") # ask the user if the picked number is larger than the guess number
            if compare == "yes": # if larger
                bottom = middle+1
                count += 1
            else:                # if smaller
                top = middle-1 
                count += 1
    more = input("Do you want to play more?(yes/no)") # ask user if he wants to play more
    if more == "no":  # if the user doesnt want to play more, assign more play to false and escape from the loop
        moreplay = False 
print("Bye-bye!")
