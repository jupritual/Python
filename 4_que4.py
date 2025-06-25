
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("input operationn(add/substract/multiply/divide)").lower()
add = num1 + num2
substract = num1 - num2 
multiply = num1 * num2
divide = num1 / num2


if operator == "add" or operator == "+":
    print(add)
elif operator == "substract" or operator == "-":
    print(substract)
elif operator == "multiply" or operator == "x":
    print(multiply)
elif operator == "divide" or operator == "/":
    print(divide)
else:
    print("You entered wrong operation")