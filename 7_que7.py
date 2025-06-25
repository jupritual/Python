def calculate_bmi(height, weight):
    bmi = weight / (height * height)
    print(f"Your BMI is: {bmi}")
h = float(input("enter your height in meters:"))
w = float(input("enter your weight:"))
calculate_bmi(h, w)