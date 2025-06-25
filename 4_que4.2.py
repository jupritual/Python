def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operator = input("enter operation (add/substract/multiply/divide): ").lower()
if operator == "add":
    print("The result is:", add(num1, num2))
elif operator == "substract":
    print("The result is:", substract(num1, num2))
elif operator == "multiply":
    print("The result is:", multiply(num1, num2))
elif operator == "divide":
    print("The result is:", divide(num1, num2))

else:
    print("error")