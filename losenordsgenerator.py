chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars2 = "1234567890"
chars3 = "!%&/()=#"
import random 
import string
password = ""
for c in range (4):
    password += random.choice(chars)
    password += random.choice(chars1)
    password += random.choice(chars2)
    password += random.choice(chars3)

password = ''.join(random.sample(password,len(password)))

f= open("losenordfil.txt","a") 
f.write(password)
f.write("\n")
