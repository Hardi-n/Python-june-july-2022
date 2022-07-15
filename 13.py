'''
Author: Kavya Jain
Date: 24-06-2022
Day: Friday
Title: Dictionary
'''
# {} are used to create dictionary
# Data is stored in the form of key and value
# dict keyword is used
# syntax: {key:value}

# print("\nPrinting only Keys")
# a = {"A":1, "B":2, "C":3}
# for i in a:
#     print(i)

# print("\nPrinting only Values")
# for i in a:
#     print(a[i])

# print("\nPrinting Keys as well as Values both")
# for i in a.items():
#     print(i)

# print("\nPrinting Keys as well as Values both")
# for i, y in a.items():
#     print("Keys:", i, ", Value:", y)


# n = int(input("How many pairs do you want in your dictionary:"))
# d = {}
# for i in range(n):
#     k = input() 
#     v = int(input()) 
#     d[k] = v
# print(d)


# c = input("Do you want to see any index value?(y/n)\n")
# if c == "y":
#     d1 = int(input("Please enter which index value do you want to print:"))
#     print(d[d1])
# else:
#     print("Okay")

dict_1={"A":"Aditya Raj",'B':20,'C':100}

print(dict_1.keys())
for i in dict_1:
  print(i)
  
print(dict_1.values(),'\n')
for i in dict_1.items():
  print(i)
  
print('\n',dict_1.get("A"))

for i,j in dict_1.items():
  print('keys',i,'Values',j)
size=len(dict_1)

usr_choi=input('Do you want to see the information of any index (y/n): ')
while usr_choi=='y' or usr_choi=='Y':
 choice=int(input('Enter the index of which you want to see the key and value: '))
 keys=list(dict_1.keys())
 values=list(dict_1.values())
 if choice>=0 and choice<size:
  print('keys',keys[choice],'values', values[choice])
 else:
   print("No item exit")

 usr_choi=input("Do you want to see the information of more index(y/n): ")
 if usr_choi=='y' or usr_choi=='Y':
   continue
 else:
   break