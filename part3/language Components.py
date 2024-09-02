"""Control flow (if statements and loops)
write a python program that asks the user for a number and determines whether it is positive, negative, or zero"""

x = int(input("enter any number")) ##taking any number from user
if(x > 0):
    print(f"{x} is positive") ##display if num is positive
elif(x < 0):
    print(f"{x} is negative") ##display if num is negative
else:
    print(f"{x} is equal to zero") ## display if num is zero 



"""Implement a loop that continues to ask the user for a number until they enter 'exit'
use 'break' to exit the loop and 'continue' to prompt for a new number if the input is not 'exit'"""

while True: ##this loop is an infinte loop
    user_input = input("enter any number (or type 'exit' to stop)")
    
    if(user_input.lower() == 'exit'): ##check if user enter 'exit' in lower case
        print("exiting the loop")
        break #to exit the loop
    
    else: ## continue the loop if exit is not entered
        num = int(user_input)
        print(f"you entered the number: {num}")
        continue # prompt for a new number if the input is not 'exit'



"""Relational and logical operators
create a python script that takes two numbers as input and prints whether both numbers are even, odd, or one of each using relational and logical operators."""

# Take two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
# Check if both numbers are odd
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
# If neither of the above conditions are true, then one is even and the other is odd
else:
    print("One number is even and the other is odd.")


"""For loop and Bitwise operators
write a python program that takes an integer input and prints its binary,octal and hexadecimal equivalents using for loop and bitwise operators."""

# function to convert into binary, octal, hexadecimal
def conversion(num, base):
    # Handle the special case where the number is 0
    if num == 0:
        return '0'
    
    digits = ''
    
    # Loop until num is reduced to 0
    while(num > 0):
        # Find the remainder of num divided by n (current least significant digit)
        rem = num % base
        # Prepend the remainder to the result string
        digits = str(rem) + digits
        num = num // base ## Update num to be the quotient of num divided by n (shift right by one digit)
    
    return digits
    

# Prompt the user to input a decimal number    
num = int(input("enter any number"))
# Print the conversions of the number to binary, octal, and hexadecimal
print(f"decimal to Binary conversion of {num} is: ",conversion(num,2))
print(f"decimal to octal conversion of {num} is: ",conversion(num,8))
print(f"decimal to hexadecimal conversion of {num} is: ", conversion(num,6))
