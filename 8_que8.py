import random
import string
l = int(input("Enter the lenth of your password:"))
char = string.ascii_letters + string.digits + string.punctuation 
password = ''.join(random.choice(char) for i in range(l))
print(password)