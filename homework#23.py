"""
- Functions -
A. Create a function named add_numbers that takes two parameters, a and b, and 
returns their sum. Test the function with values 10 and 15.

def add_numbers(a, b):
    return a + b

print(add_numbers(10, 15))


B. Create a function named calculate_area that calculates the area of a rectangle. 

Add a docstring explaining what the function does and use type annotations for parameters 
and the return value.


def calculate_area(a: int, b:int):
    '''This function calculates the area of rectangle.
    The user should enter 2 sides. Then the function
    will multiple these 2 sides and we get a result'''
    area = a * b
    return area

print(calculate_area(3, 4))

OR


def calculate_area():
    a = float(input("Enter the first side:"))
    b = float(input("Enter the second side:"))
    area = a * b
    return area

print(calculate_area())

C. Write a function that takes a string as a parameter and returns the count of vowels (a, e, i, o, u)
in the string.

def vowels_count():
    vowels_num = 0
    sentence = input("Enter the sentence:")
    vowels_lst = ["a", "e", "i", "o", "u"]
    for char in sentence:
        if char in vowels_lst:
            vowels_num+=1
    print(f"The vowels number in this list is {vowels_num}")


vowels_count()

D. Write a function that calculates the factorial of a given number n using a for loop.

def factorial_calculator():
    factorial = 1
    n = int(input("Enter the number whose factorial you want to calculate:"))
    for i in range(1, n+1):
        factorial*=i
    print(factorial)

factorial_calculator()

OR

def factorial_calculator(n):
    factorial = 1
    for i in range(1, n+1):
        factorial*=i
    print(factorial)

factorial_calculator()

OR


def factorial_calculator(n):
    factorial = 1
    for i in range(1, n+1):
        factorial*=i
    return factorial

print(factorial_calculator(5))



E. Write a function that takes a string as a parameter and returns True if the string is a palindrome 
(reads the same forwards and backwards), and False otherwise.

def palindrom_checker(word: str):
    return word == word[::-1]
        
    
print(palindrom_checker())

F. Write a function that takes a string as a parameter and returns the reverse of the string. 
Use a for loop to iterate through the characters in the string.

def reverse_string(n):
    reverse_result = ""
    for char in n:
        reverse_result = char + reverse_result
    print(reverse_result)

reverse_string("Hello")


G. Write a function that takes a number as a parameter and prints whether it's positive, negative, 
or zero using if-elif-else statements.

def number_checker(n: float):
    if n > 0:
        print("This number is positive")
    elif n < 0:
        print("This number is negative")
    else:
        print("Zero!")

number_checker(5)


H. Write a function that takes a list of boolean values as a parameter and returns the count of True
and False values in the list. Use a for loop and if statements.

def bul_checker(lst: list):
    '''This function count the number of True
    and False in your programm'''
    true_count = 0
    false_count = 0
    for char in lst:
        if char == True:
            true_count+=1
        else:
            false_count+=1
    print(f"the number of True is {true_count}, the number of False is {false_count}")

lst = [True, False, True, False, True]
bul_checker(lst)


I. Write a function that checks if a given number is a prime number. Return True if it's prime, and 
False if it's not. Use a for loop and conditionals.

def prime_number_checker(n: int):
    k = 0
    for i in range(2, n):
        if n % i == 0:
            k+=1
    if k > 0:
        return False
    else:
        return True

print(prime_number_checker())


J. Write a function that takes a list of numbers as a parameter and returns the largest number in the 
list. Use an if statement to track the largest number.

def largest_number(lst: list):
    num = 0
    for i in lst:
        if i > num:
            num = i
    return i
    
lst = [1, 9, 65, 158966]
print(largest_number(lst))



K. Write a program that calculates the sum of all even numbers from 1 to a given number n. Use a for 
loop and an if statement.

def even_numbers_sum(n: int):
    ''' his function calculates the sum of 
    all even numbers 
    from 1 to a given number n'''
    summ = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            summ+=i
    return summ

print(even_numbers_sum(9))

L. Write a program that prints numbers from 1 to 10. For multiples of 3, print "Fizz" instead of the 
number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".


for num in range(1, 16):
    if num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    print(num)

Quiz.
1. What is a function in Python?
   
    b) A block of reusable code
    
    

2. How do you define a function in Python?
    a) def function_name()
  

3. What is the purpose of a return statement in a function?
  
    c) To return a value from the function
    

4. Can a Python function return multiple values?
    a) Yes
    

5. What is a docstring in Python?
 
    c) A comment used for explaining the purpose and usage of a function, class or module
    
6. How do you write a docstring in a Python function?
    a) Using triple single-quotes or triple double-quotes at the beginning of the function
   

7. What is the purpose of type annotations in Python?
   
    d) To comment on the function's implementation

8. How do you add type annotations to a function in Python?
   
    b) By writing the types as comments next to the variables
    

9. What is a type hint in Python?
   
    b) A suggestion for the expected type of a variable or expression
  

10. What is the benefit of using type hints in Python?
   
    b) It makes the code more readable and self-explanatory
   

11. How do you specify the return type of a function in a type hint?
    a) By using -> followed by the return type
 

12. What is the purpose of using type annotations for function parameters and return values?
   
    c) To make the code more understandable and maintainable


13. What does the following Python code snippet do?
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")

    a) Defines a function to greet a person by name
  

14. What is the primary purpose of the following Python function?
    def calculate_average(numbers):
        \"\"\"Calculates the average of a list of numbers.\"\"\"
        total = sum(numbers)
        count = len(numbers)
        return total / count


    c) To calculate the average of a list of numbers
    

15. What is the output of the following Python code snippet?
    def is_even(num):
        return num % 2 == 0

    print(is_even(4))

    a) True
  

16. How do you call the function is_even from question 15 to check if the number 7 is even?
    a) is_even(7)
   

17. What does the following Python code snippet do?
    def print_numbers(n):
        for i in range(n):
            print(i)

    print_numbers(5)

    a) Prints the numbers 0 to 4

18. What does the following Python code snippet do?
    def absolute_value(num):
        if num >= 0:
            return num
        else:
            return -num

    result = absolute_value(-5)

    
    b) Calculates the absolute value of a number
   

19. What is the output of the following Python code snippet?
    def greet(time):
        if time < 12:
            return "Good morning!"
        elif time < 17:
            return "Good afternoon!"
        else:
            return "Good evening!"

    print(greet(10))

    a) Good morning!
  

20. What does the following Python code snippet do?
    def square(num):
        return num ** 2

    numbers = [1, 2, 3, 4]
    squared_numbers = [square(num) for num in numbers]

    b) Squares each number in the list numbers


21. What is the purpose of using functions with loops in Python?
    
    b) To modularize code and avoid repetition
  

22. What is the purpose of using functions with if statements in Python?
    a) To define the if statement's condition
    
"""