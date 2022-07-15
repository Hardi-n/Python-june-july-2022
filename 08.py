'''
Author: Kavya Jain
Date: 17-06-2022
Day: Friday
Title: Functions
'''
# -----------------calculator----------------
from cmath import sqrt


# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a / b

# print("\n-----------------------------------------")
# print("|\t\tCALCULATOR\t\t|")
# print("-----------------------------------------\n")
# n1 = int(input("\nEnter 1st no.: "))
# n2 = int(input("Enter 2nd no.: "))

# while(True):
#     o = input("\nWhich operation you want to perform: ")
#     if o == "+":
#         print(n1, " + ", n2, " = ", add(n1, n2))
#     elif o == "-":
#         print(n1, " - ", n2, " = ", sub(n1, n2))
#     elif o == "*":
#         print(n1, " * ", n2, " = ", mul(n1, n2))
#     elif o == "/":
#         print(n1, " / ", n2, " = ", div(n1, n2))
#     else:
#         print("Enter valid operation")
    
#     ny = input("\nDo you want to perform further calculation?\n")
#     if ny == "yes":
#         continue
#     else:
#         break


# -----------------Factorial of a number-------------------
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
# num = int(input("Enter a number whose factorial you want: "))
# print("Factorial of", num, "is:", fact(num))

# ------------------Perimeter, Area, volume of various shapes------------------
def square(s):
    print("\nArea of square = ", s * s)
    print("Perimeter = ", 4 * s)
    print("Volume of cube = ", s * s * s)

def Rectangle(l, b, h):
    print("\nArea = ", l * b)
    print("Perimeter = ", 2 * (l + b))
    print("Volume of cuboid = ", l * b * h)

def circle(r):
    print("\nArea = ", 3.14 * r * r)
    print("Perimeter = ", 2 * 3.14 * r)
    print("Volume of sphere = ", (4 / 3) * 3.14 * r * r *r)

i = input("Enter shape's name: ")
if i == "Square":
    a = int(input("Enter side: "))
    square(a)
elif i == "Rectangle":
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    h = int(input("Enter height: "))
    Rectangle(l, b, h)
elif i == "circle":
    r = int(input("Enter radius: "))
    circle(r)
else:
    print("Enter valid shape name")