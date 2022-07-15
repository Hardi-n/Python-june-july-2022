'''
Author: Kavya Jain
Date: 23-06-2022
Day: Thursday
Title: list
'''
# import pyttsx3 
# engine = pyttsx3.init() 
# engine.say("Hello Anaaya") 
# engine.runAndWait()
'''
1 WAP to sum all the items in the list
2 WAP to multiply all items in the list
3 WAP to get the largest no. in the list
4 WAP to get the smallest no. in the list
5 WAP to remove duplicate item from a list
6 WaP to check whether the list is empty or not
7 WAP to shuffle a list
8 WAP to copy a list
9 WAP to get the difference between two list
10 WAP to append a list to the second list
'''
 

# 1
l1 = [1, 2, 3, 4, 5]
print(l1)
s = 0
for i in l1:
    s = s + i
print("\nAddition of all items in the list", s)

# 2
l1 = [1, 2, 3, 4, 5]
s = 1
for i in l1:
    s = s * i
print("\nMultiplication of all items in the list", s)

# 3
l1 = [1, 5, 42, 6, 2]
lar = l1[0]
for i in l1:
    if i > lar:
        lar = i
print("\nLargest number among the list", lar)

# 4
l1 = [1, 2, 3, 4, 5]
sma = l1[0]
for i in l1:
    if i < sma:
        sma = i
print("\nSmallest number among the list", sma)

# 5
l1 = [1, 2, 3, 1, 2, 4, 5, 4, 2]
print("\nList Before removing duplicates", l1)
tl = []
for i in l1:
    if i not in tl:
        tl.append(i)
print("\nList After removing duplicates ", tl)

# 6
# l1 = []
l1 = [1, 45, 52, 6, 45]
if len(l1) == 0:
    print("\nList is empty")
else:
    print("\nList is full")

# 7
from random import shuffle
l1 = [1, 2, 3, 4, 5]
shuffle(l1)
print(l1)
    
# 8
# l1 = [1, 2, 3, 4, 5]
# l = []
# for i in l1:
#     if i not in l:
#         l.append(i)
# print()
# print(l)

l1 = [1, 2, 3, 4, 5]
# l = list(l1)
l = l1.copy()
print("Copied List",l)

# 9
l11 = [1, 2, 3, 4, 5]
l22 = [14, 42, 73, 94, 25]


# 10
l1 = [1, 2, 3, 4, 5]
l = []
for i in l1:
    if i not in l:
        l.append(i)
print()
print(l)