from time import sleep
import time
choice=input("enter your choice")
choice=int(choice)

def function(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


print("the program is about to start.")
time.sleep(5)
function(choice)


#gets a practice on functions

ip = input("what is the target IP address? ")

def nmap(ip):
    print("attacking {ip}")

nmap(ip)



