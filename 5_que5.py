import random 
number = random.randint(1, 10)
guess_num = int(input("Enter your guessed number: "))
if guess_num == number:
    print("You guessed it right")
else:
    print("you guessed it wrong, the correct number was", number)