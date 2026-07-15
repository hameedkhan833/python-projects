# --------------CALCULATOR PROGRAM--------------


print("CALCULATOR")
while True:
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num1 : "))
    operation = input("Select operation : (+,-,*,/) : ")

    # Addition
    if operation == "+":
        print("Addition : ", num1 + num2)
          
    # Subtraction
    elif operation == "-":
        print("Subtraction : ", num1 - num2)   

    # Multiplication
    elif operation == "*":
        print("Multiplication : ", num1 * num2)     

    # Division
    elif operation == "/":
        if num2 == 0:
            print("Division by zero is not possible!")
        else:
            print("Division:", num1 / num2)
        
    

    else :    
        print("Enter valid operator!")

    terminate = input("Type 'Exit' to terminate, or hit 'enter' to continue : ")
    if terminate.capitalize() == "Exit":
        break     

     


    
