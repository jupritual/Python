import random
tie = 0
user = 0
comp = 0
while True:
    spr = ["scissors", "paper", "rock"]
    user_input = input("Choose [scissors, paper, rock] Or 'exit' to quit game\nEnter:").lower()
    if user_input == "exit":
        print("Thanks for playing game")
        break
    if user_input not in spr:
        print("You enterd wrong play")
        continue
    else:
        computer = random.choice(spr)
        print(f"you choose {user_input.capitalize()}\nComputer choose {computer.capitalize()}")
        if user_input == computer:
            print("game is tied")
            tie += 1
        elif (user_input == "scissors" and computer == "paper") or \
             (user_input == "paper" and computer == "rock") or \
             (user_input == "rock" and computer == "scissors"):
            print("You won")
            user += 1
        else:
            print("You lose")
            comp += 1
        print(f"Score: You:- {user} comp:- {comp} Tie:- {tie}")
    if user == 3:
        print("You defeat computer")
        break
    elif comp == 3:
        print("You got defeated by computer")
        break