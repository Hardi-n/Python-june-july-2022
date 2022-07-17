import random
from traceback import print_tb
mylist = []
for i in range(1, 201):
    x = random.randint(1, 10)
    mylist.append(x)
print("list contains these number:", mylist)
b = int(input("Enter the number you want to check how many times it occurs in list (1-9:)"))

print(mylist.count(b))
    
mylist1= list(set(mylist))
print(mylist1)