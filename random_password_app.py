import random
import string
pass_length = int(input("Please enter the number of characters : ")) 

special_characters = string.punctuation
digits = string.digits
letters = string.ascii_letters

pass_characters = letters + digits + special_characters

password = ''
for i in range(pass_length):
    password += ''.join(random.choice(pass_characters))

print("this your password : ", password)


