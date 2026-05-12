import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!\n")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n--- Expense List ---")

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(f"""
Expense #{index}
Title    : {expense['title']}
Amount   : ${expense['amount']}
Category : {expense['category']}
Date     : {expense['date']}
""")
        total += expense['amount']

    print(f"Total Expenses: ${total}\n")


# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("""
====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()