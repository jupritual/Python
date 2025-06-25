import random
number = random.randint(1,10)
for done in range(3):
    guessed_num = int(input("Enter your guessed number: "))
    if guessed_num == number:
        print("😍You guessed it right damn")
        break
    else: 
        chance = 2 - done
        if chance > 0:
            print(f"🙁you guessed it wrong you have {chance} chance left, try again")
        else:
            print(f"😭you lost, correct number was {number} (noob)")
        