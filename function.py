#function is block of code
#we can pass data known as parameters
#function can return data as a result only when we called it
#keyword of function ---> def
#round brackets () are used
#colon(:) must

#HOW TO CREATE A FUNCTION
'''def s1(): #fuction create
    name=input("Enter your name: ")
    trade=input("Enter your trade: ")
    reg=int(input("Registration number: "))
    print(name)
    print(trade)
    print(reg)
s1() #function call'''

#arguments
def mystd(s1,s2,s3):   #here name is argument of s2 function
    print("The intelligen student is ",s1) 
mystd(s1="daljeet",s2="kavya",s3="subhi")
'''s2("daljeet")  #information is written when we call function
s2("kaur")
s2("DALJEET")
s2("KAUR")'''

def place(state="punjab"):
    print("i am from",state)
place()
place("UP")
place("Haryana")


#return values
def arithmetic(x):
    return 5*x
print(arithmetic(2))
print(arithmetic(3))
print(arithmetic(4))
print(arithmetic(5))
print(arithmetic(6))