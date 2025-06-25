def calculated_marks(marks):
    if marks > 100 or marks < 0:
        print("You've entered wrong marks")
    elif marks >= 90:
        print("Your grade is A+ ✅")
    elif marks >= 80:
        print("Your grade is A")
    elif marks >= 70:
        print("Your grade is B")
    elif marks >= 60:
        print("Your grade is C")
    elif marks >= 50:
        print("Your grade is D")
    else:
        print("You're Fail In the exam")
m = int(input("Enter Your Marks here: "))
calculated_marks(m)