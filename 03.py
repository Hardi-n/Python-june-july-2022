'''
Author: Kavya Jain
Date: 11-06-2022
Day: Saturday
Title: Rock, paper, scissors game
       Number guessing game
'''

while(True):
    print("\n----------------------")
    print("Rock, Paper, Scissors!")
    print("----------------------")

    p1 = input("\nEnter your name: ")
    p2 = input("Enter your name: ")

    print("\nPlayer 1:", p1)
    print("Player 2:", p2)

    print("\nEnter a choice (stone, paper, scissors): ")

    t1 = input("Enter 1st player's turn: ")
    t2 = input("Enter 2nd player's turn: ")

    print("\nFirst player choice: ", t1)
    print("Second player choice: ", t2)

    if((t1 == "paper" and t2 == "stone") or (t1 == "scissors" and t2 == "paper") or (t1 == "stone" and t2 == "scissors")):
        print("***********THE WINNER IS", p1, "**************")
    elif((t2 == "paper" and t1 == "stone") or (t2 == "scissors" and t1 == "paper") or (t2 == "stone" and t1 == "scissors")):
        print("\nTHE WINNER IS", p2)
    else:
        print("\n***********DRAW************\n")
    print("\nTHANK YOU!!!")
    
    
    a = input("\nDo you want to play again?(y/n)\n")
    if a == "y":
        continue
    else:
        break


# ------------------number guessing game------------------
# a = input("\nEnter your name: ")
# b = input("\nDo you want to play number guessing game?\n")
# while(b == "yes"):
#     c = int(input("Choose any number between 1 to 10: "))
#     if c == 4:
#         print("Match found!!!")
#     else:
#         print("Match not found")
#     o = input("\nDo you want to play again?\n")
#     if o == "yes":
#         continue
#     else:
#         break
    


# print("Stone Paper Scissors")
# print("Enter choice \n 1 -> Rock, \n 2 -> paper, and \n 3 -> scissor \n")

# kavya = int(input("Kavya: "))
# jain = int(input("Jain: "))

# if kavya == 1:
#     print("Kavya: Rock")
# elif kavya == 2:
#     print("Kavya: paper")
# else:
#     print("Kavya: scissor")

# if jain == 1:
#     print("Jain: Rock")
# elif jain == 2:
#     print("Jain: paper")
# else:
#     print("Jain: scissor")

# if kavya == jain:
#     print("Draw")
# elif (kavya == 1 and jain == 2):
#     print("Jain won")
# elif (kavya == 2 and jain == 1):
#     print("Kavya won")
# elif (kavya == 1 and jain == 3):
#     print("Kavya won")
# elif (kavya == 3 and jain == 1):
#     print("Jain won")
# elif (kavya == 1 and jain == 3):
#     print("Kavya won")
# elif (kavya == 3 and jain == 1):
#     print("Jain won")
# elif (kavya == 2 and jain == 3):
#     print("Jain won")
# elif (kavya == 3 and jain == 2):
#     print("Kavya won")
