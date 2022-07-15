'''
Author: Kavya Jain
Date: 16-06-2022
Day: Thursday
Title: Function
'''
# It is block of code
# def-keyword
# It will be executed ony when we call it
# : must be placed after def statement

# def f1():
#     print("Inside Function")
# f1()

# def f2():
#     nam = input("Enter your name: ")
#     tra = input("Enter your Trade: ")
#     roll = int(input("Enter your Roll no.: "))
#     print("\nYou entered\n")
#     print("Name: ", nam)
#     print("Trade: ", tra)
#     print("Roll no.: ", roll)
# f2()

# ------------Passing Arguments---------------
# def f3(name, Trade, roll):
#     print(name, Trade, roll)
# f3("Kavya", 2010217, "CDE")
# f3("Ubuntu", 2010237, "CDE")

# def f4(a, b, c):
#     print("\nIntelligent Student: ", b)
# f4("Ubuntu", "Happy", "Kaddu")

# def f4(a, b, c):
#     print("\nIntelligent Student: ", b, "\n")
# s1 = input("\nEnter Student 1 name: ")
# s2 = input("Enter Student 2 name: ")
# s3 = input("Enter Student 3 name: ")
# f4(s1, s2, s3)


# -------------Default Argumnets----------
# def f5(pl="Mumbai"):
#     print("My Favourite plcae is ", pl)
# f5("Delhi")
# f5()
# f5("Sangrur")
# f5("Kashmir")
# f5("Chandigarh")

# ------------------Returning a value from function-----------------
# def f6(x):
#     return 5 * x
# print(f6(1))
# print(f6(2))
# print(f6(3))
# print(f6(4))
# print(f6(5))
# print(f6(6))
# print(f6(7))
# print(f6(8))
# print(f6(9))
# print(f6(10))

# def add(x, y):
#     return x + y
# print("Addition: ", add(10, 5))

# def mul(x, y):
#     return x * y
# print("Multiplication: ", mul(10, 5))

# def sub(x, y):
#     return x - y
# print("Subtraction: ", sub(10, 5))

# def div(x, y):
#     return x % y
# print("Division: ", div(10, 5))

# ------------------Task----------------

# ---------------maximum of three numbers---------------
def max3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1, " is greater") 
    elif n2 > n1 and n2 > n3:
        print(n2, "is greater")
    else:
        print(n3, "is greater")

# max3(4, 5, 1)

a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
c = int(input("Enter 3rd no.: "))

max3(a, b, c)


# ---------------Odd or Even----------------
def oddEven(n):
    if n % 2 == 0:
        print(n, "is a even no.")
    else:
        print(n, "is an odd no.")

num = int((input("Enter a no.: ")))
oddEven(num)