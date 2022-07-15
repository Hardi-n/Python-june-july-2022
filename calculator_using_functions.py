def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

print("==================================CALCULATOR==================================")

print("Select any operation: ")
print("1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. REMAINDER")
print("\n")
while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        num1=int(input("Enter a: "))
        num2=int(input("Enter b: "))
        print("ADDITION: ",add(num1,num2))
        print("\n")
    elif choice==2:    
        num1=int(input("Enter a: "))
        num2=int(input("Enter b: "))   
        print("SUBTRACTION: ",sub(num1,num2))
        print("\n")
    elif choice==3:
        num1=int(input("Enter a: "))
        num2=int(input("Enter b: "))
        print("MULTITION: ",mul(num1,num2))
        print("\n")
    elif choice==4:
        num1=int(input("Enter a: "))
        num2=int(input("Enter b: "))
        print("DIVIION: ",div(num1,num2))
        print("\n")
    elif choice==5:
        num1=int(input("Enter a: "))
        num2=int(input("Enter b: "))
        print("REMAINDER: ",rem(num1,num2))
        print("\n")
        another_calculation=input("Next Calculation (yes/no): ")
        if another_calculation=="no":
          print("THANK YOU!!")
          break
    else:
        print("INVALID INPUT!!")