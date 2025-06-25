
while True: 
    user = int(input("1.add\n2.substrac\n3.multiply\n4.divide\n5.exit\nEnter sequence Number: "))
    if user == 5:
        print("Hey, goodbye")
        break 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    one = num1 + num2
    two = num1 - num2
    three = num1 * num2
    four = num1 / num2 
      
    if user == 1:
        print(f"Your answer is:{one}")
    elif user == 2:
        print(f"Your answer is:{two}")
    elif user == 3:
        print(f"Your answer is:{three}")
    elif user == 4:
        print(f"Your answer is:{four}")
    else:
        print("You entered wrong sequence number")

    
