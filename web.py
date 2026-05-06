
from flask import Flask
def main():
    print(f"Flie name {__name__}")

if __name__ == "__main__":
    print("Ran directly")
else:
    print("ran from import.")