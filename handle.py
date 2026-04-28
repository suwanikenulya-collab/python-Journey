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




