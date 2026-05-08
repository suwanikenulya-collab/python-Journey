import random
import string

print("=== Secure Password Generator ===")

# Ask the user for password length
length = int(input("Enter password length: "))

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display generated password
print(f"Generated Password: {password}")