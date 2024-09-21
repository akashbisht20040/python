#Lecture_2 
#string methods/function


x="hello world"
x=x.replace('l','w')
print(x)

print(id(x))
print(type(x))


x=x.replace("hewwo","hello")
x=x.replace("worwd","world")
print(x)

# string is immutable , therefore ID change nhi hogi , it will remain permanent

# length of string
print(len(x))


str2="0123456789"
print(len(str2))
# the range is from 0 to N-1

# access the first index of the string
print(str2[0])

print(str2[0:5])

# to print the complete string using slicing 
print(str2[0:len(str2)])

# or
print(str2[0:])


#Type conversion in python

# x=10/2
# x

# need to get output only 5 instead of 5.0
x=int(10/2)
print(x)

print(bool(0))

print(bool(-1))
# In Python, any non-zero value is considered True when evaluated as a boolean. This includes negative numbers like -1.

a=-10001.000012
print(abs(a))

print(round(a,2))


#List in python

a=[1,2,3,4]
print(a)

print(a[0])


# changing the value of index 0
a[0]=10
print(a)
# this prove that list are mutable 

# using inbuilt function
print(sum(a))


#Input function

name=input("Enter your name: ")
print(f"my name is {name}")

#finding the size of function help in optimizationp purpose

import sys # Sys are in built function

x=42
size=sys.getsizeof(x)
print(f"Size of x:{size} bytes")

# syntax of function


def display(testvar):
    print(f"Value is {testvar} ")
    print(f"Value  of ID is {id(testvar)}")
    print(f"Value  of ID is {type(testvar)}")

a=int(input("enter the number"))
display(a)
display(a)