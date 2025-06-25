import random
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}
rolls = 0
while True:
    user = input("Wanna roll the dice 'yes'/'no\nEnter: ").lower()
    if user == "no":
       print("Thanks for rolling dice.")
       break
    elif user == "yes":
        rolled = random.randint(1, 6)
        rolls += 1
        print(f"the dice rolled and stopped at {rolled} {dice_faces[rolled]}")
        print(f"🎯 Total rolls: {rolls}\n")
    else:
        print("You entered wrong option, please try again")
