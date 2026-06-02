questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What's the most abundant gas in Earth's atmosphere?",
    "Which planet is the hottest?",
    "How many bones are in the human body?"
)

options = (
    ("A. 116", "B. 117", "C. 118"),
    ("A. Whale", "B. Crocodile", "C. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. CO2"),
    ("A. Mercury", "B. Venus", "C. Earth"),
    ("A. 256", "B. 207", "C. 209")
)

answers = ("C", "C", "A", "B", "B")

score = 0
question_num = 0

for question in questions:
    print("------------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1

print("------------------------------------------")
print(f"Final Score: {score}/{len(questions)}")