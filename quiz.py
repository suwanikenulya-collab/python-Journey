score = 0

# Question 1
print("Question 1: What is 2 + 2?")
x = input("Enter the answer: ")

if x == "4":
    score = score + 1
    print(f"You are right and the score is {score}")
else:
    print("Wrong answer.")

# Question 2
print("Question 2: Capital of Sri Lanka?")
y = input("Enter the answer: ")

if y.lower() == "colombo":
    score = score + 1
    print(f"You are right and the score is {score}")
else:
    print("Wrong answer.")

print(f"Final score: {score}")