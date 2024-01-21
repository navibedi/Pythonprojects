#These are the variables for all the user interactions
a = int(input("what is your first number?: "))
b = int(input("what is your second number?: "))
z = input ("Which mathematical operation do you want to do?: ")

# Addition formula created using function:
def add(x, y):
    addition = x+y
    return addition

# Subtraction formula created using function:
def sub(x, y):
    subtraction = x-y
    return subtraction

# Multiplication formula created using function:
def mult(x, y):
    multiplication = x * y
    return multiplication

# Division formula created using function:
def div(x, y):
    if y != 0:
        return x/y
    else:
        print ("Invalid reponse, the answer is 0")

#Here the 'if' statement is used to identify all the mathmetical operations when inputted in 'z' variable
if z == "+":
    result = add(a, b)
    print ("You answer is", add(a, b))
elif z == "-":
    print ("Your answer is", sub(a,b))
elif z == "*":
    print ("Your answer is", mult(a,b))
elif z == "/":
    print ("Your answer is", div(a,b))
else:
    print("invalid operation")
