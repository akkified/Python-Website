def calc():
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
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

print(calc())