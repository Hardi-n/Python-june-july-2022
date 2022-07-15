#list are used to store multiple items(data types) like int, char, float, complex etc. in single variable. 
# [] square brackets are used
#list items are ordered 
# indexing : positive and negative
#["hi", 23, 34, 33, 2.3, 34.5, "bye"]
#  0    1    2   3    4    5     6---->+tive indexing
#  -7  -6   -5  -4   -3   -2    -1<----   -tive indexing
#benefit of indexing : we can access any element by use their index number.

'''fruits=["apple","mango","banana","cherry"]#string
print(fruits)
print("\n")
# to print list in vertical form we have to use loop
fruits=["apple","mango","banana","cherry"]#string
for x in fruits:
    print(x)
fruits=["apple","mango","banana","cherry"]
print(*fruits, sep= "\n" )

string=["Daljeet","kaur","kaddu","kavya"]
print(string)
for x in string:
    print(x)

integer=[11,22,33,44,55,66,77,88,99]
print(integer)
for i in integer:
    print(i)

float=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
print(float)
for i in float:
    print(i)

mix=["Daljeet kaur",2010237,"CDE", 20, 90.5 ]
print(mix)
for x in mix:
    print(x)


#to check the length of list we use ---->>length function---->keyword --> len
fruits=["apple","mango","banana","cherry"]#string
print(len(fruits))



#to check the type of list we use ---->>type function---->keyword --> type
fruits=["apple","mango","banana","cherry"]#string
print(type(fruits))

#========================how to convert a tuple value into list=============================
#list constructor is used and double round brackets 
fruits=list(("apple","mango","banana","cherry"))
print(len(fruits))

fruits=["apple","mango","banana","cherry"]#string
print(fruits[-1])
'''

mix=["Daljeet kaur",2010237,"CDE", 20, 90.5 ]
#positive indexing
print("POSITIVE INDEXING")
print("=====================\n")
print(mix[0])
print(mix[1])
print(mix[3])
print(mix[4])
print("\nNEGATIVE INDEXING")
print("=====================\n")
#negative indexing
print(mix[-1])
print(mix[-2])
print(mix[-3])
print(mix[-4])
print(mix[-5])