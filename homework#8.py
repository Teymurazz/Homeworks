"""
Note. Try to clear the terminal if appropriate.

- Comments -
If it's appropriate:
A. One-line comment 
B. Multi-line comment

- Programs -
A. Write a program that asks user for their personal data (name, age, nationality).
The program should decoratively print this values to the terminal.

name = input("Enter your name:")
age = input("Enter your age:")
nationality = input("Enter your nationality:")
info = f"Your name is {name} *** Your age is {age} *** Your nationality is {nationality}"
print(info)

B. Write a simple calculator program that can only sum the values.
If user inputs 10 and 5, the program should print 15

first_number = float(input("enter first number:"))
second_number = float(input("enter second number:"))
result = first_number + second_number
print(result)

C. Write a string calculator program that adds strings to strings.
If user inputs:
1. 'Hello' and 'World', the program should print 'HelloWorld'.
2. 10 and 5, the program should print 105.
3. 'Hello' and 10, the program should print Hello10

first_string = input("enter first string:")
second_string = input("enter second string:")
result = first_string + second_string
print(result)

- Modules -
A. Which Python module provides a collection of string constants, such as ascii_letters?

string.ascii_letters

B. If you want to create a password generator that includes both uppercase 
and lowercase letters, which constant from the 'string' module might be useful?

string.ascii_lowercase
string.ascii_uppercase

C. What is the purpose of using constants like ascii_letters from the string module in Python programming?

you can create your own string by adding the necessary characters to it.

D. What is '
The getpass() function of the getpass module prints a hint and prompts the user for a password without repeating it.

- Python Tricks -
A. Suppose you have the following variables:
a = "Hello"
b = 5

One-line change the value of 'a' to value of 'b', and vice versa.
Print their values

a = "Hello"
b = 5
a,b = b,a
b,a = a,b
print(a,b)
print(b,a)

- Constants -
A. Create a constant variable related to Mathematics.

PI = 3.14

B. Create a constant variable related to Physics.

G = 9.8

C. Create a constant variable related to Price.

PRICE_OF_OIL = 100

D. Create a constant variable related to Time.

HOURS_IN_DAY = 24

E. Are Python constants really carry constant values?

NO

- Math -
A. Round down 57_999.99 to the nearest integer.

print(round(57_999.99))

B. Find the square root of 57_999.99. Round it to one decimal point.

import math
num = math.sqrt(57_999.99)
print(round(num,1))

C. Round up 0.0592481 to the nearest integer.

print(round(0.0592481)

D. Find the value of 5.5 raised to power 5.

print(pow(5.5,5))

- NoneType -
A. What is None in Python? How is this value described in other programming
languages?
This is data type. 0

B. What is the best practices of using None in Python?

for reserve any variable, which we'll use in code, for example  value = None

C. How Python evaluates the NoneType? (True / False)

False

D. Create any NoneType object. Print it.

value = None
print(value)

- Built-ins -
A. Create two variables (x and y). Using built in function raise 'y' to 'x' power.

x = 2
y = 3
print(pow(y,x))

B. Using built in function and variables from Task A raise 'x' to 'y' power.

print(pow(x,y))

C. Ask user for two integers. Raise first integer to second integer power.

first_integer = int(input("Enter first integer:"))
second_integer = int(input("Enter second integer:"))
result = pow(first_integer,second_integer)
print(result)

- String Formattings -

A. You have the math's Pi number. Using f-strings, round it to two decimal points.

Pi = f"{Pi:.2f}"

B. Write a program that represents 5_000_000 as (5,000,000) in console     

number = 5000000
formatted_number = format(number, ",")
print(formatted_number)

C. Write a program that calculates the percentage of apples left in the fridge.
Initially you got 28 apples, but you ate 4. Using f-strings 

apple_numbers = 28
ated_apple_numbers = 4
left_apple_numbers = apple_numbers - ated_apple_numbers
percentage = left_apple_numbers / apple_numbers * 100
print(f"the percentage of the apples left in the fridge is {percentage} ")

- Chat GPT's Homework -

1. What does the random.choice(seq) function do?

B) Selects a random element from the sequence seq.             


2. How do you generate a random integer between 5 and 10 (inclusive) 

using random.randint(a, b)                               

from random import randint

number = randint(5,10)

3. Write a code snippet that generates a random float between 0 and 1 
(exclusive) using random.random(). 

number = random.random(0,1)

4. What does the random.sample(seq, k) function do?
        
D) Returns the first k elements from the sequence.

5. Calculate the square root of 25 using the math.sqrt() function.

from math import sqrt

print(math.sqrt(25))

6. How do you access the value of pi using the math module?

from math import pi

7. If you have a float value x = 7.6, how would you round it up to the nearest 
integer using the math.ceil() function?

import math
print(math.ceil(7.6))

8. Write a Python program that generates and prints 5 random integers between 
50 and 100 (inclusive) using the random.randint() function.  

from random import randint

number = random.randint(50,100)

9. Write a Python program that takes a floating-point number as input and prints 
its square root using the math.sqrt() function.

from math import sqrt
number = float(input("enter number:"))
print(math.sqrt(number))

10. Implement a Python "Roll Dice" program that simulates rolling a six-sided die. 
The program should return a random number between 1 and 6.

from random import randint

n = randint(1, 6)
print(n)


- Interview Questions -
1. Reverse a string with slicing method.

print(string[-1::-1])

Quiz.
1. What does the None keyword represent in Python?
   
    c) A reserved keyword for creating new variables
    

2. Which type is assigned to a variable that has no value assigned to it in Python?
 
    b) NoneType
   

3. What is the result of evaluating the expression: type(None)?
    a) <class 'NoneType'>
   

4. Which statement assigns the value None to the variable 'result'?
 
    b) result = None
    

5. What is the correct way to check if a variable value is set to None?
   
    d) if value is None ?

6. Can None be used in arithmetic operations in Python?
    
    b) No, trying to perform arithmetic with None will result in an error.
    

7. What does the math.floor(x) function do?
    
    b) Returns the largest integer less than or equal to x.
   

8. Which of the following is the correct way to import the 'math' module in Python?
   
    b) import math
    c) from math import *
  

9. The math.ceil(x) function does what?
    
    b) Returns the value of x rounded up to the nearest integer.
   

10. What does the math.pow(x, y) function do?
   
    c) Calculates the power of x raised to the yth power.
    

11. The math.sqrt(x) function is used to:
    a) Calculate the square root of x.


12. What is the output of the following code:
    import math
    value = 3.05
    print(math.floor(value))

    a) 3
   

13. What is the output of the following code:
    from math import pi
    a = round(pi, 2)
    print(a * 2)

    c) 6.28
   

14. What is the purpose of the random.choice(seq) function?
    
    b) It selects a random element from the sequence seq.
    

15. Which of the following methods is used to select multiple unique random 
elements from a sequence?
   
    b) random.sample(seq, count)
    

16. How would you import the random module correctly in Python?
   
    d) import random

17. If you want to generate a random integer between 1 and 100 (inclusive), 
which random module method would you use?
    a) random.randint(1, 100)
   

18. In Python, what is the process of combining multiple strings into one?
    a) Concatenation
  
19. What does the ascii_letters constant include?
    
    c) Both uppercase and lowercase letters
  

20. Which PEP provides recommendations and guidelines for writing clean, readable, and maintainable Python code?
    
    b) PEP 8
    

21. What is the primary purpose of the "as" keyword in Python's "import" statement?
    a) It renames the module being imported.
    b) It allows importing multiple modules at once.
    c) It imports all the functions and classes from the module.
    d) It enables conditional imports based on runtime conditions.   +++
"""