#NAME : Akash Bisht
#SAP ID : 590010802
#Faculty_Name : Prateek Gautam
#COURSE : PYTHON PROGRAMMING



"""1. Basic function implementation
Write a function greet that takes two arguments ; name(a string) and greeting (a string with a default value of "Hello".This function should return a greeting message
greet("Alice") # Output: "Hello Alice"

greet("Bob", "Good Morning") # Output: "Good Morning Bob"""


def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

# calling the function 
print(greet("Alice"))          
print(greet("Bob", "Good Morning"))




"""2. Named Arguments
Create a function create_profile that takes arguments for name, age, and city as named arguments . the function should return a string like "Name":alice,age:25,city:New York. Ensure that the age arguments has a default value of 18
create_profile(name="John", city="Chicago") # Output: "Name: John, Age: 18, City: Chicago"

create_profile(name="Emma", age=22, city="Los Angeles") # Output: "Name: Emma, Age: 22, City: Los Angeles"""


def create_profile(name, city, age=18):
    return f"Name: {name}, Age: {age}, City: {city}"

# Function call karenge direct 
print(create_profile(name="Akash", city="Dehradun"))  
print(create_profile(name="Sapna", age=21, city="Dehradun"))





"""3 **using *args and kwargs:
Write a function sum_number that takes any number in positional arguments(args) and keyword arguments(*kwargs) . It should
1. Return the sum of all *args if they are numbers
2. Return a dictionary all keywords arguments
sum_numbers(1, 2, 3) # Output: 6

sum_numbers(1, 2, x=4, y=5) # Output: (6, {'x': 4, 'y': 5})""" 


def sum_numbers(*args, **kwargs):
    total_sum = 0
    
    for arg in args:
        # Check if the argument is a number (int or float)
        if isinstance(arg, (int, float)):
            # agar number Integer hai toh add karna hai
            total_sum += arg

    dict1 = {}  # blank diictionary
    for key in kwargs:
        dict1[key] = kwargs[key]

    return total_sum, dict1


print("Sum:",sum_numbers(1, 2, 4))  
print("Keyword:" ,sum_numbers(1, 2, x=4, y=5))




"""4. Lambdas and Map :
Write a function that uses map and a lambda to return a list where each element is squared"""


def square_elements(val):
    return list(map(lambda x: x**2, val))

n = [1,2,3,4,5,6,7,8,9]
input1 = square_elements(n)
print(input1)




"""5. Filter and Lambdas :
Write a function that filters out all odd numbers from a list using filter and a lambda function"""


def filter_odds(val):
    return list(filter(lambda x: x % 2 == 0, val))

n = [1,2,3,4,5,6,7,8,9,14,60]
filtered_numbers = filter_odds(n)
print(filtered_numbers)




"""6. Basic List Comprehension :
Create a list comprehension that takes a list of numbers and returns a list of their squares"""


def square_elements(val):
    return [x**2 for x in val]

n = [2,4,5,7,8,]
square = square_elements(n)
print(square)




"""7.List Comprehension with Condition :
Use a list comprehension to create a list of even numbers from 1 to 20"""


even_numbers = [x for x in range(1,21) if x%2 == 0]

print(even_numbers)




"""8. Using os and time Modules :
Write a function file_operations that creates a directory named "test_folder" using os.makedirs(). Then, pause the execution for 3 seconds using time.sleep(), and finally, delete the directory using os.rmdir()"""


import os
import time

def file_operations():
    # Create a directory named "test_folder"
    folder_name = "test_folder"
    os.makedirs(folder_name)
    print(f"Directory '{folder_name}' created.")
    
    # Pause for 3 seconds
    time.sleep(3)
    
    # Delete the directory
    os.rmdir(folder_name)
    print(f"Directory '{folder_name}' deleted.")




"""9. Importing Specific Functions :
Q. Write a Python script that imports only sleep from the time module and renames it to pause. Use it to pause execution for 2 seconds and print "Paused execution..."""


from time import sleep as pause

pause(2)

print("Paused execution...")




"""10. Recursive Function with args and kwargs (Flattening a List) :
Write a recursive function flatten_list that can flatten a nested list of any depth using args and kwargs"""


def flatten_list(*args):
    flatten = []
    for item in args:
        if isinstance(item, list):
            flatten.extend(flatten_list(*item))
        else:
            flatten.append(item)
            
    return flatten

nested_list = [1, [2, [3, 4]], 5, [6, [7, [8]]]]
flat_list = flatten_list(*nested_list)
print(flat_list)
