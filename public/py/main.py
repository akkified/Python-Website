from pyweb import pydom

def calc(num1,num2):
    operation = input("What operation do want to do? ")
    if operation == "Add":
        return(num1 + num2)
    elif operation == "Subtract":
        return(num1 - num2)
    elif operation == "Multiply":
        return(num1 * num2)
    elif operation == "Divide":
        return(num1/num2)
    else:
        print("You entered the wrong operation!")

print(calc(float(input("What is your first number? ")),float(input("What is your second number? "))))