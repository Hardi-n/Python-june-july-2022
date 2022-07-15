'''
Author: Kavya Jain
Date: 21-06-2022
Day: Tuesday
Title: Lists
    - creation of list
    - accessing elements of list
    - indexing:- postive and negative
    - len() and type() function
'''
# we use [] bracket to make a list
# list is used to store multiple items in one variable
# list is mutable(modifiable)
# list items are ordered
# We can perform various operations on list. Ex:-
# append-add at end
# insert-add at particular index
# indexing - positive and negative
#         1   , 2, 3,  4
# li = ["Kavy", 4, 5, 1511]
#        -4   ,-3,-2,  -1

# fruits = ["Apple", "Banana", "Mango", "Cherry"]
# print(len(fruits))
# print(type(fruits))
# print(fruits)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

# for i in fruits:
#     print(i)

# l1 = ["Kavy", "Anaaya", "Jain"]
# print(l1)
# print(*l1, sep="\n")
# for i in l1:
#     print(i)
# print()

# l2 = [11, 15, 1511]
# print(l2)
# print(*l2, sep="\n")
# for i in l2:
#     print(i)
# print()

# l3 = [12.3, 75.69, 78.6]
# print(l3)
# print(*l3, sep="\n")
# for i in l3:
#     print(i)
# print()

# l4 = ["Anaaya", 15, 11.5]
# print(l4)
# print(*l4, sep="\n")
# for i in l4:
#     print(i)
# print()

# --------------tuple--------------
# () bracket are used to make tuple
# It is used to store multiple data items
# tuples are immutable(cannot modify)

# fruits = ("Apple", 45, 4263.58, False)
# print("\nTuple:", fruits)
# fruits = list(("Apple", 45, 4263.58, False)) #list constructor
# print("\nList:", fruits)
# print("\nPrinting through positive indexing: ")
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print("\nPrinting through negative indexing: ")
# print(fruits[-4])
# print(fruits[-3])
# print(fruits[-2])
# print(fruits[-1])

food = ["Pizza", "Burger", "Noodles", "Samosa"]
drinks = ["Coca-Cola", "Pepsi", "Sprite", "Limca"]
chocolate = ["Kit-Kat", "Milky Bar", "Diary Milk", "Bar-One"]
a = input("Which item do you want(food, drinks, chocolate)?\n")
b = int(input("Which index you want to print\n"))
if a == "food":
    print(food[b])
elif a == "drinks":
    print(drinks[b])
elif a == "chocolate":
    print(chocolate[b])
else:
    print("Enter valid choice.")

l = input("Which item's length do you want to know(food, drinks, chocolate)?\n")
if l == "food":
    print("Length of", l, "is", len(food))
elif l == "drinks":
    print("Length of", l, "is", len(drinks))
elif l == "chocolate":
    print("Length of", l, "is", len(chocolate))
else:
    print("Enter valid choice.")

a1 = input("Name the list in which you want to append\n")
b1 = input("Name the item you want to append\n")
if a1 == "food":
    food.append(b1)
    print(food)
elif a1 == "drinks":
    drinks.append(b1)
    print(drinks)
elif a1 == "chocolate":
    chocolate.append(b1)
    print(chocolate)
else:
    print("Enter valid choice.")

a1 = input("Name the list in which you want to insert\n")
b1 = input("Name the item you want to insert\n")
c1 = int(input("Enter the index at which you want to insert\n"))
if a1 == "food":
    food.insert(c1, b1)
    print(food)
elif a1 == "drinks":
    drinks.insert(c1, b1)
    print(drinks)
elif a1 == "chocolate":
    chocolate.insert(c1, b1)
    print(chocolate)
else:
    print("Enter valid choice.")