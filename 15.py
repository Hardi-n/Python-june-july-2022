'''
Author: Kavya Jain
Date: 27-06-2022
Day: Monday
Title: File handling
'''
# 3 modes- (w)write, (r)read, (a)append
# syntax
# variablename = open("filename", 'mode')
# variablename.write("content")
# variablename = file.read()
# variablename.close()

# ---------Write to a file-----------
# file = open("file.txt", 'w')
# file.write("Hello\n")
# file.write("Kavya\n")
# file.close()

# -------------read to a file-------------
# file = open("file.txt", 'r')
# data = file.read()
# print(data)
# file.close()

# ----------line by line------------
# file = open("file.txt", 'r')
# for line in file:
#     print("~", line)
# file.close()

# -----------append to a file------------
# file = open("file.txt", 'a')
# file.write("Good Morning\n")
# file.write("Bye\n")
# file.close()

k = open("f3.txt", 'w')
c1 = input("Enter your name: ")
k.write(c1)
k.close()

k = open("f3.txt", 'a')
c2 = input("Enter your last name: ")
k.write(c2)
k.close()

k = open("f3.txt", 'r')
da = k.read()
print(da)
k.close()


f = open("f2.txt","w")
print("\nEnter 5 names: ")
for i in range(5):
       n = input()
       f.write(n)
       f.write('\n')
f.close()
f = open("f2.txt","r")
print("\nYou entered:")
d = f.read()
print(d)
f.close()
