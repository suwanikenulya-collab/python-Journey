# TRY / EXCEPT NOTES (Error Handling in Python)

# Basic structure
try:
    x = int(input("Enter a number: "))
    print(10 / x)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

except Exception as e:
    print("Something went wrong:", e)


# ELSE block (runs if no error)
try:
    num = int(input("Enter another number: "))
except ValueError:
    print("Not a number!")
else:
    print("Good input:", num)


# FINALLY block (always runs)
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")


# Why this matters in cybersecurity:
# - Prevents crashes in tools
# - Handles network errors safely
# - Avoids exposing sensitive system details
# - Keeps scripts stable during attacks or failures