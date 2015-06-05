class Animal:
    def __init__(self, name):
        self.name = name         # instance variable unique to each instance
    def guess_who_am_i(self):    # guess method
        print ("I will give you 3 hints, guess what animal I am\n")
        if self.name == "elephant":  # for elephant object
            questions = ['I have exceptional memory','I am the largest land-Living mammal in the world','I have large and thin ears']
        elif self.name == "tiger":   # for tiger object
            questions = ['I am the biggest cat','I come in black and white or orange and black','I have been known to reach speeds up to 65 kph (40 mph)']
        elif self.name == "bat":     # for bat object
            questions = ['I use Echo-location','I can Fly','I see well in dark']
        for i,question in enumerate(questions):
            print (question)
            guess = input ("Who am I?: ")
            if guess == self.name :
                print ("You got it! I am", self.name, "\n")
                break
            else:
                print ("Nope, try again!\n")
                if i == 2:
                    print ("I'm out of hints! The answer is:" , self.name ,"\n")

e = Animal("elephant")  # define object from class
b = Animal("bat")
t = Animal("tiger")

e.guess_who_am_i()      # call method for object
t.guess_who_am_i()
b.guess_who_am_i()


