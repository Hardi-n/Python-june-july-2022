'''
Author: Kavya Jain
Date: 20-06-2022
Day: Monday
Title: 
'''
# for i in range(1, 4):
#     for j in range(1, 4):
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |      |     ")
    print("\t {}  |  {}  |  {} ".format(values[0], values[1], values[2]))
    print('\t_____|_____ |_____')
    print("\t     |      |     ")
    print("\t {}  |  {}  |  {} ".format(values[3], values[4], values[5]))
    print('\t_____|_____ |_____')
    print("\t     |      |     ")
    print("\t {}  |  {}  |  {} ".format(values[6], values[7], values[8]))
    print("\t     |      |     ")
    print("\n")
# while(True):
print_tic_tac_toe()



p1 = input("Enter your name(X): ")
p2 = input("Enter your name(0): ")

a = input("")
b = input("")

s1 = 0
s2 = 0

# if values[0] == values[1] == values[2] == "X":
#     s1 += 1 
# elif values[0] == values[1] == values[2] == "0":
#     s2 += 1 
# elif values[0] == values[3] == values[6] == "X":
#     s1 += 1 
# elif values[0] == values[3] == values[6] == "0":
#     s2 += 1 
# elif values[6] == values[7] == values[8] == "X":
#     s1 += 1 
# elif values[6] == values[7] == values[8] == "0":
#     s2 += 1 
# elif values[2] == values[5] == values[8] == "X":
#     s1 += 1 
# elif values[2] == values[5] == values[8] == "0":
#     s2 += 1 
# elif values[0] == values[4] == values[8] == "X":
#     s1 += 1 
# elif values[0] == values[4] == values[8] == "0":
#     s2 += 1 
# elif values[2] == values[4] == values[6] == "X":
#     s1 += 1 
# elif values[2] == values[4] == values[6] == "0":
#     s2 += 1 