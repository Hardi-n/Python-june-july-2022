a=input("Student name: ")
b=input("Registration number: ")
c=input("Trade: ")
Total_marks=int("500")

print("Enter the marks of student below: ")
CS224=int(input("COMPUTER NETWORKS: "))
CS223=int(input("COMPUTER ORGANIZATION AND ARCHITECTURE: "))
CS222=int(input("NETWORK OPERATING SYSTEM : "))
CS221=int(input("OBJECT ORIENTED PROGRAMMING: "))
CS225=int(input("SYSTEM INSTALLATION AND MAINTAINANCE: "))

sum=(CS224+CS223+CS222+CS221+CS225)
print("MARKS: ",sum)

avg=(sum)/5
print("AVERAGE: ",avg)

if avg>=81 and avg<=100:
    print("GRADE:A+")
elif avg>=70 and avg<=80:
    print("GRADE:A")
elif avg>=61 and avg<=69:
    print("GRADE:B+")
elif avg>=56 and avg<=60:
    print("GRADE:B")
elif avg>=51 and avg<=55:
    print("GRADE:C+")        
elif avg>=41 and avg<=50:
    print("GRADE:C")
elif avg>=35 and avg<=40:
    print("GRADE:D")
elif avg>=0 and avg<=34:
    print("GRADE:E")
else: 
    print("Invalid input!!")