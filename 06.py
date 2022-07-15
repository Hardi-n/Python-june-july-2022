'''
Author: Kavya Jain
Date: 15-06-2022
Day: Wednesday
Title: Patter Printing
       Quiz
'''
# program to print the number pattern in the form of half pyramid
#    1 2 3 4           i    j               j <= i
#  1 *                 1    1               j <= 1
#  2 * *               2    1, 2            j <= 2
#  3 * * *             3    1, 2, 3         j <= 3
#  4 * * * *           4    1, 2, 3, 4      j <= 4
# n = int(input("Enter the no. of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j <= i:
#             # print(i, end="")
#             print(j, end="")
#         else:
#             print(" ", end="")
#     print()

# ----------Task-----------
res = 0
a = input("Do you want to play QUIZ game?\n")
while(a == "yes"):
    q1 = input("\n1. What is a correct syntax to output \"Hello World\" in Python? \na) print(\"Hello World\")\nb) echo(\"Hello World\");\nc) echo \"Hello world\"\nd) p(\"Hello World\")\nYour answer: ")
    if q1 == "a":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q2 = input("\n2. How do you insert COMMENTS in Python code?\na) /*cmt*/\nb) #cmt\nc) //cmt\nd) !cmt\nYour answer: ") 
    if q2 == "b":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q3 = input("\n3. Which one is NOT a legal variable name?\na) my_var\nb) Myvar\nc) my-var\nd) _myvar\nYour answer: ")
    if q3 == "c":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q4 = input("\n4. How do you create a variable with the numeric value 5?\na) Both b and c\nb) x = int(5)\nc) x = 5\nd) None of these\nYour answer: ")
    if q4 == "a":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q5 = input("\n5. What is the correct file extension for Python files?\na) .pyt\nb) .pt\nc) .py\nd) .pyth\nYour answer: ")
    if q5 == "c":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q6 = input("\n6. How do you create a variable with the floating number 2.8?\na) Both b and c\nb) x = 2.8\nc) x = float(2.8)\nd) None of these\nYour answer: ")
    if q6 == "a":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q7 = input("\n7. In Python, 'Hello', is the same as \"Hello\"\na) False\nb) True\nYour answer: ")
    if q7 == "b":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q8 = input("\n8. Which operator is used to multiply numbers?\na) %\nb) X\nc) -\nd) *\nYour answer: ")
    if q8 == "d":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q9 = input("\n9. Which operator can be used to compare two values?\na) ><\nb) <>\nc) ==\nd) =\nYour answer: ")
    if q9 == "c":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")
    q10 = input("\n10. How do you start writing an if statement in Python?\na) if x > y then:\nb) if(x > y)\nc) if x > y:\nd) if x > y\nYour answer: ")
    if q10 == "c":
        print("Correct answer")
        res += 1 
    else:
        print("Wrong answer")

    print("\n----------Your score: ", res, " / 10------------")
    cont = input("\nDo you want to play again?\n")
    
    if cont != "yes":
        break
    else:
        continue
    # Mansikanojoa24530@gmail.com