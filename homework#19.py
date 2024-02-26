"""
- Error Handling (Assert & Raise) -
A. Write a Python program that takes two parameters, a and b, 
and returns the result of a divided by b. Use the "assert" keyword to 
verify that b is not equal to zero before performing the division. 
If b is zero, raise an AssertionError with the message "Division by 
zero is not allowed."

a = int(input("<<"))
b = int(input("<<"))
assert b!= 0, ZeroDivisionError
c = a / b
print(c)


B. Write a Python program that takes an age as a parameter.
Use the "raise" keyword to raise a ValueError if the age is less than 
0 or greater than 120. The error message should be 
"Invalid age: Age must be between 0 and 120."

age = int(input("<<"))
if age < 0 or age > 120:
    raise ValueError ("Invalid age: Age must be between 0 and 120.")

- Projects -
Proj A.
Write a Python program that takes a user's age as input and performs 
the following validations using "assert" and "raise" keywords:
1. Ensure that the age is a positive integer.
2. Ensure that the age is less than or equal to 120 (a common maximum age assumption).

users_age = int(input("<<"))
assert users_age > 0, ValueError ("Only positive numbers!")
if users_age > 120:
    raise ValueError ("The number should be between 0 and 120")
print(users_age)


Proj B.
Write a Python program that takes two numbers as input from the 
user and performs a mathematical operation (e.g., addition, subtraction, 
multiplication, or division). Use "assert" and "raise" keywords to 
handle the following cases:
1. Ensure that the input numbers are numeric.
2. Ensure that division by zero is not allowed.

a = input("Enter the first number:")
b = input("Enter the second number:")
if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
    raise ValueError("Input numbers must be numeric")
if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
print(f"sum = {a + b}")
print(f"div = {a / b}")
print(f"sub = {a - b}")
print(f"mult = {a * b}")


Proj C.
Write a Python program that takes a list and an index as input 
from the user and attempts to access the element at that index 
in the list. Use "assert" and "raise" keywords to handle the following cases:
1. Ensure that the index is within the valid range for the given list.
2. Ensure that the input is an integer.


user_list = input("Enter a list: ").split()
user_index = int(input("Enter an index: "))
assert isinstance(user_index, int), "Index should be an integer"
assert 0 <= user_index < len(user_list), "Index out of range"
print(user_list[user_index])

Quiz.
1. What is the purpose of the "assert" keyword in Python?
    a) To raise an exception and handle errors.


2. Which of the following statements is true regarding the "assert" keyword?
  
    c) It is used to catch and handle errors.
   

3. When using the "assert" keyword, what happens if the condition is false?
    
    b) The program continues to the next line of code.
    

4. What is the primary purpose of the "raise" keyword in Python?
  
    c) To raise a specific exception manually.
  

5. Which of the following is true regarding the "raise" keyword?
    
    b) It can be used to raise both built-in and custom exceptions.
 

6. What is the output of the following code? 
    try:
        assert 2 + 2 == 5, "Math is broken!"
    except AssertionError as e:
        print(e)
    
    a) Prints: Math is broken!
  

7. What is the output of the following code?
    try:
        assert 1 == 0, "Assertion failed"
    except ZeroDivisionError:
        print("ZeroDivisionError occurred")
    except AssertionError as e:
        print(e)
    finally:
        print("Finally block executed")

    a) Prints: Assertion failed, Finally block executed
   

8. What is the output of the following code?
    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        elif age >= 120:
            raise ValueError("Age cannot be 120 or above")
        else:
            print("Age is valid")

    try:
        validate_age(150)
    except ValueError as e:
        print(e)

 
    b) Prints: Age cannot be 120 or above
  
"""