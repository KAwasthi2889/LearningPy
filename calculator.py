num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Which operator do you want to use? ")
if op == '+' :
    print("Value of", num1, op, num2, "is", num1 + num2)
if op == '-' :
    print("Value of", num1, op, num2, "is", num1 - num2)
if op == '*' :
    print("Value of", num1, op, num2, "is", num1 * num2)
if op == '/' :
    print("Value of", num1, op, num2, "is", num1 / num2)
