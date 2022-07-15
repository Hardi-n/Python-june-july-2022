print("============================PYTHON QUIZ===========================")
a=input("Enter your First Name: ")
b=input("Enter you Last Name: ")
c=input("Enter your Registration number: ")
d=input("Enter your Trade: ")
print("\n")
score=0
print("Do you want to play a quiz game?\n1. Yes\n2. No")
choice=int(input("Your Choice: "))
while choice==1:
    print("==========================QUIZ START==========================")
    print("TICK THE CORRECT OPTION OF FOLLOWING QUESTIONS:- ")
    print("QUESTION 1. Which type of Programming does python suports?")
    q1=int(input("1) Object-Oriented Programming\n2) Structured Programing\n3) Fuctional Programming\n4) All of above\nYour choice:  "))
    if q1==4:
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer! \n Correct answer is 4) All of above")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")    
    print("QUESTION 2. Is python is case-senstive language?")
    q2=int(input("1) Yes\n2) No\nYour Choice: "))
    if q2==1:
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer! \nCorrect answer is 1) Yes")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")   
    print("QUESTION 3. Which is the correct extension of python file?")
    q3=int(input("1) .python\n2) .pl\n3) .py\n4) .p?\nYour Choice: "))
    if q3==3:
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer!\nCorrect answer is 3) .py")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 4. Which of the following character is used to give single line comment?")
    q4=int(input("1) #\n2) //\n3) /*\n4) !\nYour Choice: "))
    if q4==1:
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer!\nCorrect answer is 1) #")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 5. Which of the following character is used to comment multiple lines")
    q5=int(input("1) ''' '''\n2) /*  */\n3) //  //\n4)none of above\nyour answer: "))
    if q5==1:
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer!\nCorrect answer is:1) ''' '''") 
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")   
    print("QUESTION 6. Which keyword is used for function in pytho language?")
    q6=int(input("1) function\n2) def\n3) fun\n4)none of above\nYour Choice: "))
    if q6==2:
        print("Correct answer!!")
        score+=1
    else:
        print("Wrong answer!\nCorrect answer is 2) def")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 7.Which of the following is used to define a block of code in Python language? ")
    q7=int(input(" 1) Indentation\n2) Key\n3) Brackets\n4) All of the mentioned\nYour Choice: "))
    if q7==1:
        print("Correct answer!!")
        score+=1
    else: 
        print("Wrong answer!!\nCorrect answer is 1) Indentation")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 8.Which of the following functions is a built-in function in python? ")
    q8=int(input("1) factorial()\n2) print()\n3)seed()\n4) sqrt()\nYour Choice: "))
    if q8==2:
        print("Correct answer!!")
        score+=1
    else:
        print("Wrong answer!!\nCorrect answer is 2) print()")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 9. Which of the following is not a core data type in Python programming?")
    q9=int(input("1) Tuples\n2) Lists\n3) Class\n4) Dictionary\nYour Choice: "))
    if q9==3:
        print("Correct answer!!")
        score+=1
    else:
        print("Wrong answer!!\nCorrect answer is 3) Class")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    print("QUESTION 10. Which type of brackets are used in functions? ")
    q10=int(input("1) {}\n2) []\n3) ()\n4) <>\nYour Choice: "))
    if q10==3:
        print("Correct answer!!")
        score+=1
    else:
        print("Wrong answer!!\nCorrect answer is 3) ()")
    print("Your Current Score is: "+str(score)+" /10")
    print("\n")
    percentage=score/10*100
    print("TOTAL MARKS: ",percentage)
    another_response=input("Do You want to Play Quiz Game again?(Yes/No): ")