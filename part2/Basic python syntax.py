"""   1. String Operations
Write a python program that takes a user's first and last name as input and prints them in reverse order with a space between them."""
name = input("enter your name: ") # Prompt the user to enter their name

fName = "" # Initialize an empty string to store the reversed name
for i in name:
    fName = i + fName #Prepend the current character to the fName 
print(f"{name} after reversing")    
print(fName)  # Print the reversed name

      #Two String methods and their purpose

# 1.Count() method:
## Python String count() function returns the number of occurrences of a substring within a String
## string count() function is case sensitive, meaning it will treat ‘a’ and ‘A’ different.
str = "Mississipi"
charCount = str.count('s')
print('number of occurence is ',charCount)


# 2.find() method:
## Python String find() method returns the lowest index or first occurrence of the substring
# if it is found in a given string. If it’s not found then it returns -1.
word = "find me if you can"
print(word.find('me'))

"""2. Numeric Data types and conversion functions
  write a python program that takes an input number from the user, converts it to different numeric data types(integer,float, and complex) and displays the converted text."""

val = int(input("enter any number"))

#converting the data type into integer
_int = int(val)
print(f"integer value is: {_int}")

#converting the data into float
_float = float(val)
print(f"float value is {_float}")

#converting the data into complex
_complex = complex(val)
print(f"complex value is {_complex}")


# Difference between integer , float and complex data types

# 1. Integer (int):
# Represents whole numbers without any fractional or decimal part. 
# They can be positive, negative, or zero.
# Example: 5, -42, 0

# => Characteristics:
# No decimal point.
# Precision is unlimited (i.e., Python integers can grow as large as the memory allows).
# Common operations: addition, subtraction, multiplication, division, modulo, exponentiation.


# 2. Float (float):
# Represents real numbers that include a decimal point. 
# These numbers have a fractional part and are used for more precise calculations.
# Example: 5.0, -3.14, 0.001

# => Characteristics:
# Contains a decimal point to separate the whole part from the fractional part.
# Floating-point numbers are represented in Python using double precision (64-bit) according to the IEEE 754 standard.
# Precision is limited by the floating-point representation (up to about 15-17 significant digits).
# Common operations: similar to integers, but also include operations with decimals and real numbers.


# 3. Complex (complex):
# Represents complex numbers, which have a real part and an imaginary part.
# The imaginary part is indicated by a j or J.
# Example: 3 + 4j, -2.5 + 3.1j

# => Characteristics:
# Composed of a real part (an int or float) and an imaginary part (a float) which is multiplied by j (the square root of -1).
# Used in mathematics and engineering to represent complex numbers.
# Common operations: addition, subtraction, multiplication, division, and other operations on complex numbers.

"""3. Simple Input and Output
create a python script that calculates the area of rectangle. The script should:
* Prompt the user to enter the length and width of a rectangle.
* calculate the area
* Display the result using print() function
* modify the rectangle area program to format the output so that it displays the area with two decimal places"""

##asking length and width from user
len = float(input("enter the length of a rectangle"))
wid = float(input("enter the width of a rectangle"))

## calculating area of rectangle
area = len * wid
# format area upto two decimal places
format_area = "{:.2f}".format(area)
print(f"area of rectangle with length {len} and width {wid} is: {format_area}")

"""The % method and print() function
write a python script that takes three numbers as input and prints their average using the % method for string formatting."""

# Take three numbers as input from the user
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

# Calculate the average
avg = (x + y + z) / 3

# Print the average using the % method for string formatting
print("The average of the three numbers is: %.2f" % avg)
