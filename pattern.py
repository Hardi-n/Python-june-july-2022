# star pattern 1
"""

*
**
***
****

"""
#
# for i in range(1,5):
#     for j in range(1,5):
#         if(j>i):
#             print(" ",end='')
#         else:
#             print("*",end='')
#     print(" ")
#


# star pattern 2
"""

    *
   **
  ***
 ****
*****

"""
# row=int(input("Enter the rows you want:"))
# col=int(input("Enter columns you want:"))
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if(j>=(row+1)-i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

# star pattern3
"""

****
***
**
*

"""
# row=int(input("Enter the rows you want:"))
# col=int(input("Enter the number of columns you want:"))
# row=row+1
# col=col+1
# for i in range(1,row):
#     for j in range(1,col):
#         if(j<=row-i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

# star pattern 4

"""

   *
  **
 ***
****  

"""
# row=int(input("Enter the number of rows you want:"))
# col=int(input("Enter the number of columns you want:"))
# row=row+1
# col=col+1
# for i in range(1,row):
#     for j in range(1,col):
#         if(j>=i):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()


# star pattern 5

"""
    *
   ***
  *****
 *******
*********

"""

row = int(input("Enter the number of rows you want:"))
# col=int(input("Enter the number of columns you want:"))
row = row+1
# col=col+1

for i in range(1, row):
    for j in range(1, (2*row)-1):
        if(j >= (i-1) and j < (2*i)):
            print("*", end='')
        else:
            print(" ", end='')
    print()
