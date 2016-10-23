print("I am thinking about a number between 1 and 100, guess it")
from random import *
random = randint(1,100)
toomuch = 100
notenough = 1
while True:
    try:
        guess= (int(input("Guess the number: ")))
        break
    except ValueError:
        print("Try again, but this time with an integer")
while (guess !=random):
    if (guess>random and guess<=toomuch and guess>=notenough):
        while True:
            try:
                guess= (int(input("You need a smaller number: ")))
                break
            except ValueError:
                print("That is not an integer")
    elif (guess<random and guess<=toomuch and guess>=notenough):
        while True:
            try:
                guess = (int(input("You need a bigger number: ")))
                break
            except ValueError:
                print("That is not an integer")
    elif (guess>toomuch):
        while True:
            try:
                guess =(int(input("That is not between 1 and 100, try again: ")))
                break
            except ValueError:
                print("That is not an integer")
    elif (guess<notenough):
        while True:
            try:
                guess =(int(input("That is not between 1 and 100, try again: ")))
                break
            except ValueError:
                print("That is not an integer")
else:
	print ("Cool")
