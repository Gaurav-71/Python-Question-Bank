import math

print("Select Geometrical Object :- \n1. Square \n2. Rectangle \n3. Triangle \n4. Circle")
choice = int(input("-> Enter Choice : "))
if choice == 1:
    print("\nArea of Square :-\n")
    length = int(input("Enter Side Length : "))
    print("Area of Square with Side length ", length," is ", pow(length, 2))
elif choice == 2:
    print("\nArea of Rectangle :-\n")
    length = int(input("Enter Length : "))
    breadth = int(input("Enter Breadth : "))
    print("Area of rectangle with length ", length, ", breadth ", breadth, " is : ", length*breadth)
elif choice == 3:
    print("\nArea of Triangle :-\n")
    height = int(input("Enter Height : "))
    breadth = int(input("Enter Breadth : "))
    print("Area of triangle with length ", height, ", breadth ", breadth, " is : ", 0.5*height*breadth)
else:
    print("\nArea of Circle :-\n")
    radius = int(input("Enter Radius : "))
    print("Area of circle with radius ", radius," is ", math.pi*pow(radius, 2))

