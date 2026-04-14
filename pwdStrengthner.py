score=0

pwd=input("Enter your password:")

if any(char.isdigit() for char in pwd):
    score =score+1

if any(char.isupper() for char in pwd):
    score =score+1

if any(char.islower() for char in pwd):
    score =score+1

if len(pwd) >= 8:
    score =score+1

special_chars = "!@#$%^&*"
if any(char in special_chars for char in pwd):
    score += 1

print("score of the password is :" ,score)

if score<=2:
    print("weak")
elif score<=4:
    print("medium")
else:
    print("strong")



