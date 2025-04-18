import random
import string

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# User input
num_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("What should be the length of each password? "))

print("\nGenerated Passwords:")

# Loop to generate passwords
for _ in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(password)
