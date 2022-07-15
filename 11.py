'''
Author: Kavya Jain
Date: 22-06-2022
Day: Wednesday
Title: Lists(insert and append function)
'''
# append-add at end
# insert-add at particular index
# remove- removes the specified item
# pop - removes specified index value
# we can add tuple in list
l1 = [42, 23]
print(l1)
l1.append(11)
print(l1)
l1.insert(0, 15)
print(l1)
l1.remove(42)
print(l1)
l1.pop(1)
print(l1)


# food = ["Pizza", "Burger", "Noodles", "Samosa"]
# drinks = ["Coca-Cola", "Pepsi", "Sprite", "Limca"]
# chocolate = ["Kit-Kat", "Milky Bar", "Diary Milk", "Bar-One"]
# a = input("\n\nWhich item do you want(food, drinks, chocolate)?\n")
# b = int(input("Which index you want to print\n"))
# if a == "food":
#     print(food[b])
# elif a == "drinks":
#     print(drinks[b])
# elif a == "chocolate":
#     print(chocolate[b])
# else:
#     print("Enter valid choice.")

# l = input("\n\nWhich item's length do you want to know(food, drinks, chocolate)?\n")
# if l == "food":
#     print("Length of", l, "is", len(food))
# elif l == "drinks":
#     print("Length of", l, "is", len(drinks))
# elif l == "chocolate":
#     print("Length of", l, "is", len(chocolate))
# else:
#     print("Enter valid choice.")

# a1 = input("\n\nName the list in which you want to append\n")
# b1 = input("Name the item you want to append\n")
# if a1 == "food":
#     food.append(b1)
#     print(food)
# elif a1 == "drinks":
#     drinks.append(b1)
#     print(drinks)
# elif a1 == "chocolate":
#     chocolate.append(b1)
#     print(chocolate)
# else:
#     print("Enter valid choice.")

# a1 = input("\n\nName the list in which you want to insert\n")
# b1 = input("Name the item you want to insert\n")
# c1 = int(input("Enter the index at which you want to insert\n"))
# if a1 == "food":
#     food.insert(c1, b1)
#     print(food)
# elif a1 == "drinks":
#     drinks.insert(c1, b1)
#     print(drinks)
# elif a1 == "chocolate":
#     chocolate.insert(c1, b1)
#     print(chocolate)
# else:
#     print("Enter valid choice.")

# a1 = input("\n\nName the list in which you want to remove element\n")
# b1 = input("Name the item you want to remove\n")
# if a1 == "food":
#     food.remove(b1)
#     print(food)
# elif a1 == "drinks":
#     drinks.remove(b1)
#     print(drinks)
# elif a1 == "chocolate":
#     chocolate.remove(b1)
#     print(chocolate)
# else:
#     print("Enter valid choice.")

# a1 = input("\n\nName the list in which you want to pop element\n")
# c1 = int(input("Enter the index at which you want to pop\n"))
# if a1 == "food":
#     food.pop(c1)
#     print(food)
# elif a1 == "drinks":
#     drinks.pop(c1)
#     print(drinks)
# elif a1 == "chocolate":
#     chocolate.pop(c1)
#     print(chocolate)
# else:
#     print("Enter valid choice.")

pen = ["Butterflow", "Hauszer", "Writometer", "Parker"]
nb = ["Classmate", "Taj white", "Camlin", "Navneet"]
pc = ["Natraj", "Apsara", "Faber Catell", "Camlin"]
penp = 10
nbp = 50
pcp = 5
a = input("\n\nWhich item do you want(Pen, Notebook, Pencil)?\n")
b = int(input("Which index you want to print\n"))
if a == "pen":
    print(pen[b])
elif a == "drinks":
    print(nb[b])
elif a == "pc":
    print(pc[b])
else:
    print("Enter valid choice.")

l = input("\n\nWhich item's length do you want to know(pen, notebook, pencil)?\n")
if l == "pen":
    print("Length of", l, "is", len(pen))
elif l == "nb":
    print("Length of", l, "is", len(nb))
elif l == "pc":
    print("Length of", l, "is", len(pc))
else:
    print("Enter valid choice.")

a1 = input("\n\nName the list in which you want to append\n")
b1 = input("Name the item you want to append\n")
if a1 == "pen":
    pen.append(b1)
    print(pen)
elif a1 == "nb":
    nb.append(b1)
    print(nb)
elif a1 == "pc":
    pc.append(b1)
    print(pc)
else:
    print("Enter valid choice.")

a1 = input("\n\nName the list in which you want to insert\n")
b1 = input("Name the item you want to insert\n")
c1 = int(input("Enter the index at which you want to insert\n"))
if a1 == "pen":
    pen.insert(c1, b1)
    print(pen)
elif a1 == "nb":
    nb.insert(c1, b1)
    print(nb)
elif a1 == "pc":
    pc.insert(c1, b1)
    print(pc)
else:
    print("Enter valid choice.")

a1 = input("\n\nName the list in which you want to remove element\n")
b1 = input("Name the item you want to remove\n")
if a1 == "pen":
    pen.remove(b1)
    print(pen)
elif a1 == "nb":
    nb.remove(b1)
    print(nb)
elif a1 == "pc":
    pc.remove(b1)
    print(pc)
else:
    print("Enter valid choice.")

a1 = input("\n\nName the list in which you want to pop element\n")
c1 = int(input("Enter the index at which you want to pop\n"))
if a1 == "pen":
    pen.pop(c1)
    print(pen)
elif a1 == "nb":
    nb.pop(c1)
    print(nb)
elif a1 == "pc":
    pc.pop(c1)
    print(pc)
else:
    print("Enter valid choice.")

# tt = penp