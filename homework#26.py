"""
- Functions -
A. Create a function 'greet_user' that takes a name as an argument and 
prints a greeting message with the provided name. The function should 
have a default parameter of "User" for the name.

def greet_user(name="User"):
    print(f"Hello {name}")

greet_user()


B. Create a function calculate_sum that calculates the sum of an 
arbitrary number of integers passed as arguments. The function should use 
the *args parameter to accept a variable number of arguments.

def calculate_sum(*args):
    return sum(args)

print(calculate_sum())

C. Create a function display_info that takes a person's information 
(name, age, and city) as keyword arguments and prints the information.

def display_info(**kwargs):
    print(kwargs)

result = display_info(name="Asif", age=25, city="Baku")
print(result)


D. Create a function make_sandwich that takes the type of sandwich, and 
optional toppings and prints the details of the sandwich. The function 
should have a default parameter for the sandwich type and use keyword 
arguments for toppings.

def make_sandwich(sandwich_type="BLT", **toppings):
    print("Sandwich Type: " + sandwich_type)
    if toppings:
        print("Toppings:")
        for key, value in toppings.items():
            print("- " + key + ": " + value)
    else:
        print("No additional toppings")


E. Create a function show_details that takes a person's name as a fixed 
parameter, followed by an arbitrary number of hobbies using the *args 
parameter. The function should print the person's name and their hobbies.

def show_details(name, *hobbies):
    print(f"person's name is {name} and his hobbies are:")
    for hobby in hobbies:
        print(hobby)


F. Implement a function sort_numbers that takes a list of numbers as an 
argument and returns a sorted list in ascending order. Use the * operator 
to unpack the list.

def sort_numbers(lst):
    return sorted(lst)


G. Create a function create_user that takes the user's name, age, and email 
as keyword arguments and prints a message welcoming the user. Ensure to handle 
missing or invalid email addresses.

def create_user(name, age, email=None):
    if email is None or "@" not in email or "." not in email:
        print("Invalid email address provided. Please provide a valid email.")
    else:
        print(f"Welcome, {name}! We are excited to have you join us.")



H. Create a function generate_invoice that generates an invoice for a customer's 
purchase. The function should take the customer's name and purchase amount as 
required arguments, with an optional discount as a keyword argument. Calculate 
the final amount after applying the discount if provided.

def generate_invoice(customer_name, purchase_amount, discount=0):
    final_amount = purchase_amount - (purchase_amount * discount)


I. Create a function create_circle that creates a circle with specified properties 
(radius and color). Use keyword arguments to allow specifying these properties and 
validate the input.

J. Implement a function calculate_score that takes a student's scores in various 
subjects as keyword arguments and calculates their total score. Use the ** operator 
to handle an arbitrary number of subject scores.

def calculate_score(**kwargs):
    total_score = sum(kwargs.values())
    return total_score


K. Write a function calculate_volume that calculates the volume of a cylinder using 
its radius and height. Use keyword arguments for the radius and height.

import math

def calculate_volume(radius, height):
    return math.pi * radius ** 2 * height


L. Create a function print_person_info that takes a person's name as a positional 
argument and their age and city as keyword arguments. Print the person's name, age, and city.

def print_person_info(name, age, city):
    print(f"Person's name is {name}, it's age is {age} and he's from {city}")


M. Implement a function show_order_details that takes the order number as a positional argument, 
followed by a dictionary of order items as keyword arguments. Print the order number and the 
items in the order.

def show_order_details(order_number, **order_items):
    print(f"Order Number: {order_number}")
    print("Order Items:")
    for item, quantity in order_items.items():
        print(f"- {item}: {quantity}")


N. Write a function that checks whether the given pattern from the user is a substring of
the 'Cybersecurity in Programming' phrase.

def pattern_check(pattern):
    phrase = 'Cybersecurity in Programming'
    if pattern in phrase:
        return True

O. Write a function that raises all numbers from the passed list to the power of two.

def raised_func(lst):
    return list(map(lambda x : x ** 2, lst))

- Lambda Functions -
A. Write a brief explanation of what a lambda function is and when it's useful.
B. Create a lambda function that adds two numbers and test it with example inputs.

add_numbers = lambda x, y: x + y
result = add_numbers(2, 3)
print(result)

C. Create a lambda function that squares a given number and test it with example inputs.

square = lambda x: x**2


D. Create a lambda function that takes three parameters (a, b, c) and calculates 'a x b + c'.

result = lambda a, b, c : a * b + c
print(result)

E. Create a lambda function that reverses a given string and test it with example inputs.

reverse_string = lambda x: x[::-1]


F. Create a lambda function that capitalizes the first letter of a string and test it with 
example inputs.

string = input("Enter string:")
capitalize_first_letter = lambda x: x[0].upper()
print(capitalize_first_letter)

G. Create a lambda function that counts the number of vowels (a, e, i, o, u) in a given 
string and test it with example inputs.

count_vowels = lambda s: sum(1 for char in s if char.lower() in 'aeiou')


H. Create a lambda function that counts the number of words in a given string and test it 
with example inputs.

def count_words(input_string):
    return len(input_string.split())

Quiz.
1. What is a lambda function in Python?
    
    b) An anonymous function defined using the def keyword.
  

2. Which of the following is a benefit of using a lambda function?
    .
    c) It is ideal for simple, one-line operations.
    

3. In Python, which type of argument requires the caller to provide a value when calling a function?
    
    b) Keyword argument
 

4. What will the following code output?
    def multiply(a, b=2):
        return a * b

    result = multiply(3)
    print(result)

    a) 6
 

5. Which of the following is a valid usage of a lambda function?
   
    d) Iterating over a list
    
6. In Python, what will the len() function return for the string "hello"?
    a) 5
 

7. What is the purpose of a function in Python?
    
    b) To perform a specific task or set of tasks.
    

8. Which of the following is true about functions in Python?
   
    b) A function can return multiple values.
  
    

9. What is the output of the following code?
    def greet(name):
        return f"Hello, {name}!"

    message = greet("Alice")
    print(message)

    a) "Hello, Alice!"
   

10. Which of the following statements about keyword arguments is true?
   
    c) Keyword arguments provide a default value if not provided by the caller.
  

11. What is the purpose of the *args parameter in a function definition?
  .
    c) To allow the function to accept an arbitrary number of positional arguments.
    

12. In a lambda function, what does 'x' represent?
    
    b) The argument being passed to the function.


13. What will the following code output?
    text = "hello lambda"
    reverse_text = (lambda x: x[::-1])(text)
    print(reverse_text)

    a) "adamal olleh"


14. What is a default parameter in a function?
    a) A parameter that is automatically assigned a value if no value is provided by the caller.
  

15. In which situation would using default parameters be most beneficial?
    
    b) When you want to assign a specific value to a parameter unless the caller provides a different value.
  
16. What is the main difference between positional and keyword arguments in Python?
   
    b) Positional arguments are mandatory, while keyword arguments are optional.
  
    
17. When should you use positional arguments over keyword arguments?
    a) When you want to provide arguments in a specific order.
    b) When you want to ensure that the caller always provides a value for that argument.
    c) When you want to allow the caller to provide arguments in any order.
    d) When you want to provide a default value for an argument.
"""