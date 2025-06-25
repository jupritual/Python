birthday_storage = {}

while True:

    print("1. Add birthday\n2. View birthday\n3. Exit")
    user_input = int(input("Enter sequence number: "))

    if user_input == 3:
        print("Exited from birthday storage") 

    elif user_input == 1:
        name = input("Enter your name: ")
        birthday = input("Enter Your birthday (dd/mm): ")
        birthday_storage[name] = birthday 
        print("birthday added successfully.\n")

    elif user_input == 2:

        if len(birthday_storage) == 0:
            print("no birthday is stored yet.\n")

        else:
            for n, b in birthday_storage.items():
                print(f"‖Birthday list‖\n{n} --> {b}\n")
                
    else:
        print("invalid sequence numbet.\n")