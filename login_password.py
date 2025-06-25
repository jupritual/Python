user_data = {}
while True:
    print("1. Login\n2. Register\n3. Exit")
    user_input = int(input("Enter sequence number: "))
    if user_input == 3:
        print("Thanks for using our Login system,")
        break
    if user_input == 1:
        print("you've choose to Login")
        username = input("Enter your username:")
        password = input("Enter your password:")
        if username in user_data:
            if user_data[username] == password:
                print("Login successful.")
            else:
                for i in range(3):
                    print("wrong password, try again.")
                    password = input("Enter your password:")
                    if user_data[username] == password:
                            print("Login successful.")
                            break
                    else:
                       print(f"❌ Wrong password. Attempts left: {2 - i}")
                else:
                    print("Too many attempts, Please try again")
        else:
            print("Username not found, register to create account")
    elif user_input == 2:
        print("You've choose to Register")
        username = input("Enter Usermame:")
        if username in user_data:
            print("The username already exist, try to login.")
        else:
            password = input("Create Password:")
            user_data[username] = password
            print("Registration successful.")
    else:
        print("You entered wrong sequence number try entering correct one")
