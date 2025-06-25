import random
comp = random.randint(1, 100)
print("Welcome to number guessing game")
print("Enter difficulty level 'easy'/'hard' ")
difficulty = input("Enter: ").lower()
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5
else:
    print("You entered wrong option, GAME OVER")
    exit()
while attempt > 0:
    guess = int(input("Guess the number: "))
    if guess == comp:
        print("You guessed it right")
        break
    if attempt == 0:
        print("GAME OVER")
        break
    elif guess > comp:
        print(f"guess lower😉")
    elif guess < comp:
        print(f"guess higher😉")
    attempt -=1 
    print(f"Attempt left {attempt}\n")
    
if attempt == 0:
    print(f"GAME OVER\nCorrect number was {comp}")