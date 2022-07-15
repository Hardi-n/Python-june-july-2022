'''
Author: Kavya Jain
Date: 10-06-2022
Day: Friday
Title: if-else
'''

# ----------Various printing methods-----------
# print("Hello")
# v1 = "Kavya"
# print(v1)
# print("Hello ", v1)


# -----------Calculator---------------
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# c = a + b
# d = a - b
# f = a * b
# g = a % b
# print(a, " + ", b, "= ", c)
# print(a, " - ", b, "= ", d)
# print(a, " * ", b, "= ", f)
# print(a, " % ", b, "= ", g)


# ---------if-else statement-----------
# a = 10
# if a == 10:
#     print("Value is 10")
# else:
#     print("Value is not 10")


# ------------voting eligibility---------------
# a = int(input("Enter your age: "))
# if a >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")


# -----------Student average----------
a = input("\nEnter your name: ")
b = int(input("Enter your roll no.: "))
c = input("Enter your trade: ")

print("\nEnter your marks: ")
CN = int(input("Computer Networks = "))
DSA = int(input("Data Structure and Algorithm = "))
COA = int(input("Computer Organization and Architecture = "))
GD = int(input("Graphics Designing = "))
AM = int(input("Maths = "))

sum = CN + DSA + COA + GD + AM

avg = sum / 5
print("Average =", avg)

prcnt = (sum / 500) * 100
print("Percentage =", prcnt)

if prcnt >= 85:
    print("Garde: A")
elif prcnt >=70:
    print("Garde: B")
elif prcnt >=65:
    print("Garde: C")
elif prcnt >=50:
    print("Garde: D")
else:
    print("Garde: Fail")