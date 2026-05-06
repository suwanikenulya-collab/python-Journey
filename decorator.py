def add (n1, n2):
    return n1 + n2
def mult (n1, n2):
    return n1 * n2
def div (n1, n2):
    return n1 / n2
def sub (n1, n2):
    return n1 - n2

def calculate(calc,n1, n2):
    return calc(n1, n2)
results= calculate(mult,3,4)
print(results)


#how function works -more
#def out():
   # print("hello")

   # def inner():
     #   print("eww")

   # if 3-2 == 1:
     #   inner()
#out()