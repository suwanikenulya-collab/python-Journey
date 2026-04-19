print("Please enter the dimentions of the room (sqft): ")


def calculate_area(k,m):
    area = k*m
    print(f"{k}x{m} = {area} you can see the area like this ")

width=int (input("Enter the room width:"))
height=int (input("Enter the room height:"))

calculate_area(width,height)