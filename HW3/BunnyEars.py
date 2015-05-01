# Recursive function that return the number of ears for bunnies

def bunny_ears(n):   # n number of bunnies
    if n <= 0:       # 0 bunny condition
        return 0
    elif n % 2 == 0: # for even numbers of bunnies
        return bunny_ears(n-1) + 2
    else:            # for odd numbers of bunnies
        return bunny_ears(n-1) + 3
x = int(input("Enter a number of bunnies: "))
print("The number of ears are:", bunny_ears(x))
