import secrets

chars = "abcdefghijklmnopqrdtuvwxyz1234567890"
password = " "

for i in range(16):
    password += secrets.choice(chars)

print("Your Password is: ", password)