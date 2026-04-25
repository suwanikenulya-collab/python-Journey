#create a dictionary that will let you add a student and their grade
#you will need a while loop to complete this task

student_grade={}

off= False #false means program should keep running
while not off:
    name=input("Enter your name:")
    grade=input("Enter your grade:")
    student_grade[name]= grade #make dictionary like name: grade
    print("student added successfully. ")
    print(student_grade)
    add_another= input("Do you want to add another student?(y/n)").lower()
    if add_another == "y":
        off= False
    else:
        off= True
        print("program done!")


