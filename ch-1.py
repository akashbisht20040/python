#Python programming

a=2
b=2
print(a+b)

#STRING IN PYTHON

# string concept in python 

mystring="Akash Bisht"
print(mystring)
print(type(mystring))

# convert function string CAPITAL LETTER
mystring=mystring.upper()  
print(mystring)

# string got converted to lower letter 
mystring=mystring.lower()
print(mystring) 

#string converted a to b
mystring=mystring.replace("a","b")  
print(mystring)

# string concatenation 
str1="Akash"
str2="Bisht"
print(str1+str2)

# space between strings
print(str1+" "+str2)

#print string multiple times
print(str1 *3)

# membership function: to check whether the item is in string or not

str1="Akash bisht"
print("Akash"in str1)  # it return true

str3="0123456789"
# to length check 
print(len(str3))

print(str3[0])

# here 10 index position value excluded
print(str3[0:10]) 

# string comparsion
str1="apple"
str2="banana"

print(str1==str2)
print(str1<str2)  # Dictonary alphabets ascending order B is greater than A

# alphabets descending orders
a="aaabc"
b="aabc"
print(a<b)

# ESCAPE CHARACTER   
str4="hi \"python\""
print(str4)

url = "C:\\Users\\akash\\OneDrive\\Documents\\python class"
print(url)


# taking input in python

name=input("Enter your name please!!!")
# or 
print("Hi "+name)
print(f"Hi {name}")

# NUMERIC operation

print(2**4)

print(2/4)

print(20//4)

print(20%4)
