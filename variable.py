# variable.py

# Taking basic user inputs
fname = input("What is your first name? ")
lname = input("What is your last name? ")

# Display full name
print("\nYour full name is:", fname + " " + lname)

# Using f-strings (modern Python way)
print(f"You can also write your name as {fname} {lname}")


print("\n- Additional Info -")

# More inputs
username = input("Enter a username: ")
pet = input("What is your pet name? ")
city = input("Which city are you from? ")

# Final output using variables
print(f"\nYour profile:")
print(f"Username: @cyber{username}")
print(f"Pet: {pet}")
print(f"Location: {city}")

print("\nThanks for using the program!")