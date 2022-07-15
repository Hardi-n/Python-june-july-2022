'''
Author: Kavya Jain
Date: 13-06-2022
Day: Monday
Title: loops
'''

# 3 things:
# - Initialization
# - Stopping Condition
# - counter(increment/decrement)

# Iterator

# 2 types of loops: for , while

'''counter = 1
while counter < 6:
    print("Hello Kavya!")
    # counter = counter + 1
    counter += 1'''

# range(start = 0, stop, step = 1)

# for counter in range(1, 6, 1):
#     print("Hello Kavya!")

# start = 1
# n = int(input("Enter a number up to which you want your loop to work: "))
# for counter in range(start, n):
#     if start % 2 == 0:
#         print(start, " is a even number")
#         start += 1
#     else:
#         print(start, " is a odd number")
#         start += 1

# counter = 1
# n = int(input("Enter a number up to which you want your loop to work: "))
# while counter < n:
#     if counter % 2 == 0:
#         print(counter, " is a even number")
#     else:
#         print(counter, " is a odd number")
#     counter += 1


# *
# * *
# * * *
# * * * *
# * * * * *

r = int(input("Enter the no. of rows: "))
c = 1
for i in range(0, r):
    for j in range(0, i):
        print("* ", end="")
    # c += 1
    print() #Add new line after each iteration of outer loop