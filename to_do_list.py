to_do_list = []
while True:
    print("Options\n1. Add task\n2. View task\n3. Delete task\n4. Exit")
    user = int(input("Enter Sequence Number: "))
    if user == 4:
        print("Exited To-do list")
        break
    if user == 1:
        add_task = input("Enter Task: ")
        if len(add_task) == 0:
            print("You entered nothing, failed to add task:")
        else:
            to_do_list.append(add_task)
            print("Task added successfully")
    elif user == 2:
        if len(to_do_list) == 0:
            print("The To-do list is empty")
        else:
            print("Your task")
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
    elif user == 3:
        if len(to_do_list) == 0:
            print("Your To-do list is empty")
        else:
            for i, task in enumerate(to_do_list, 1):
                print(f"{i}. {task}")
            try:
                delete_task = int(input("Enter task number to delete:"))
                if 1 <= delete_task <= len(to_do_list):
                    removed_task = to_do_list.pop(delete_task - 1)
                    print(f"removed: {removed_task}")
                else:
                    print("You entered wrong task number")
            except ValueError:
                print("You enterd wrong value")
    else:
        print("You entered wrong sequence number")