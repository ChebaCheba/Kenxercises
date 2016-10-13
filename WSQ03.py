print("Zup")
while True:
    try:
        x = int(input("Gimmie da initial NUMBER:"))
        break
    except ValueError:
        print("You clearly do not know what a NUMBER is")
while True:
    try:
        y = int(input("Gimmia another one:"))
        break
    except ValueError:
        print("You did it good the first time, what happened?")
    pass
def suma (x,y):
	return ("Sum:", int(x) + int(y))
def substraction (x,y):
	return ("Substraction:", int(x) - int(y))
def multiplication (x,y):
	return ("Multiplication:", int(x) * int(y))
def division (x,y):
	return("Division:", int(int(x) / int(y)))
def remainder (x,y):
	return("Remainder:", int(x) % int(y))
print (suma(x , y))
print (substraction(x , y))
print (multiplication(x , y))
print (division(x , y))
print (remainder(x , y))
