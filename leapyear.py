year = int(input())
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("yes this is a leap year")
else:
    print("No this isn't a leap year")
    