# print("Enter a number:")
a = int(input("ENter a number:"))
b = str(input("choose a calculation symbol(+,-,*,/):"))
c = int(input("ENter another number:"))
if(b == "+"):
    print("sum of numbers", a+c)
elif(b == "-"):
    print("subtractoin of numbers:", a-c)
elif(b=="*"):
    print("multiplication of numbers:",a*c)
else:
    print("division of two numbers is:",a/c)