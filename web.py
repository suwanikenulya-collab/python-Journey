# Import the Flask class from the flask module/library
from flask import Flask


# Define a function called main
def main():

    # Print the value of __name__
    # __name__ is a special Python variable
    # It tells whether the file is being run directly or imported
    print(f"File name {__name__}")


# Check if this Python file is being run directly
# When a file is run directly, Python sets __name__ = "__main__"
if __name__ == "__main__":

    # This line runs only if the file is executed directly
    print("Ran directly")

# If the file is imported into another Python file,
# this else block will run
else:

    # This line runs when the file is imported
    print("ran from import.")