# ---------------Basic Calculator---------------
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
operation = input("Enter operation(+, -, *, /) : ")

if operation == "+":
    print("Addition : ", num1 + num2)
elif operation == "-":
    print("Subtraction : ", num1 - num2)
elif operation == "*":
    print("Multiplication : ", num1 * num2)
elif operation == "/":
    print("Division : ", num1 / num2) 
else:
    print("Enter valid operator!")     
