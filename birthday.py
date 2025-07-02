from plyer import notification
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
def send_birthday_email(name, date, your_email, app_passeord, to_email):
    subject = (f"Its {name}'s birthday🥳🥳")
    body = (f"Hey its a remainder that today{date} is {name}'s birthday")
    message = MIMEMultipart()
    message["from"] = your_email
    message["to"] = to_email
    message["subject"] = subject
    
    message.attach(MIMEText(body, "plain")) 
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(your_email, app_passeord)
        server.send_message(message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:",e)
file_name = "birthday.txt"

def call_birthday():
    birthdays = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                name, date = line.strip().split(":")
                birthdays[name] = date
    return birthdays

def save_birthday(birthdays):
    with open(file_name, "w") as f:
        for name, date in birthdays.items():
            f.write(f"{name}:{date}\n")

birthday_storage = call_birthday()

while True:

    print("1. Add birthday\n2. View birthday\n3. Check today's birthday\n4. show days left for birthdays\n5. Remove birthday\n6. Exit")
    user_input = input("Enter sequence number: ")

    if user_input == "6":
        print("Exited from birthday storage") 
        break

    elif user_input == "1":
        name = input("Enter your name: ")
        birthday = input("Enter Your birthday (dd/mm): ")
        birthday_storage[name] = birthday 
        save_birthday(birthday_storage)
        print("birthday added successfully.\n")

    elif user_input == '2':

        if len(birthday_storage) == 0:
            print("no birthday is stored yet.\n")

        else:
            print("‖Birthday list‖")
            for name, date in birthday_storage.items():
                print(f"{name} --> {date}\n")
        
    elif user_input == "3":
        today = datetime.now().strftime("%d/%m")
        found = False

        for name, date in birthday_storage.items():
            if today == date:
                print(f"Today's {name}'s birthday.\n")
                found = True
                send_birthday_email(name=name,
                                    date=date,
                                    your_email="divyamwankhade56@gmail.com",
                                    to_email="divyamwankhade56@gmail.com",
                                    app_passeord="ykehiecapxcajvga")
                notification.notify(
                    title=f"🎉 It's {name}'s Birthday!",
                    message=f"Wish {name} today! 🎂",
                    timeout=10
                )

                
        if not found:
            print("No one's birthday today.\n")        

    elif user_input == "4":
        print("📅 Days Left Till Each Birthday:")
        today = datetime.now()

        for name, date in birthday_storage.items():
            day, month = map(int, date.split("/"))
            birthday_this_year = datetime(year=today.year, month=month, day=day)

            if birthday_this_year < today:
                birthday_next_year = datetime(year=today.year +1, month=month, day=day)

            else:
                birthday_next_year = birthday_this_year
                
            day_left = (birthday_next_year - today).days
            print(f"{name}'s birthday in {day_left} day(s)")

    elif user_input == "5":
        if  len(birthday_storage) == 0:
                print("birthday list is empty")

        else:
            remove = input("Enter name to remove birthday: ").lower()
            if remove in birthday_storage:
                del birthday_storage[remove]
                save_birthday(birthday_storage)
                print(f"successfully removed {remove}'s birthday\n")
            else:
                print(f"{remove} isn't in birthday list\n")

    else:
        print("invalid sequence number.\n")

