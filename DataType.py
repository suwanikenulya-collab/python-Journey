#data types
# 1. strings
#print(type("Hello World"))
#print ("hello world"[0]) # we can type a letter by it's index

#2. integer
#print (type(5))

#3. float
#print (type(5.67))

#4. boolian
#true or false

#-----note is done---

fnum= input("enter a number")
snum= input ("enetr a second number")

if fnum > snum:
    print ("the first number is larger.")
elif fnum < snum:
    print ("the second number is smaller.")
else:
    print("the numbers are the same.")


    #loops

#if statement
score = input("enter a score")
score = int(score)

if score >= 90:
    print ("the score is A")
elif score >=80:
    print ("the score is B")
elif score >=70:
    print ("the score is C")
elif score >=60:
    print ("the score is D")
else:
    print ("the score is F")

#nested loop -if statement


mark= input("enter a mark")
mark = int(mark)

if mark >= 90:
    age= int (input("enter a age"))
    if age <18:
        print ("the age is less than or equal to 18")
    else:
        print ("the age is greater than or equal to 18")
elif mark >= 80:
    age = int(input("enter a age"))
    if age < 18:
        print("the age is less than or equal to 18")
    else:
        print("the age is greater than or equal to 18")
else:
    print ("you are need to do the test again.")


