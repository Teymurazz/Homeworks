"""
- I/O -
Warning! 1. You should set appropriate variable names each time when
you create a variable. 2. You should ask users appropriate questions.
3. Pay attention to the question style, try to decorate it.

A. Write a program that asks user for his/her name.
Print the name in capitalized form, so if the user
types in 'aysel', we should see 'Aysel' on the console.

name = input("Enter your name:")
name = name.capitalize()
print(name)


B. Ask user for their age. Subtract this age from 50.

age = int(input("enter your age:"))

sub_age = 50 - age

print(sub_age)

C. Ask user for their address, favorite color, car brand.
Using multi-line string formatting print this values using it
in a sentence.

address = input("Enter your address:")
favorite_color = input("Enter your favorite color:")
car_brand = input("Enter your car brand:")
print(f"My friend lives in Baku at {address}. His favorite color is {favorite_color}. He has a car {car_brand}.")

D. Write a calculator that plusses user's inputted numbers.

print(eval(input("a+b")))

E. Write a calculator that subtracts user's inputted numbers.

print(eval(input("a-b")))

F. Write a calculator that multiplies user's inputted numbers.

print(eval(input("a*b")))
G. Write a calculator that divides user's inputted numbers.

print(eval(input("a//b")))

H. Ask user for 3 different numbers. Multiply first two numbers
and then divide the result by the third inputted number.

a = input("enter first number:")

b = input("enter second number:")

c = input("enter third number:")

print(eval(input("a*b/c")))  or just       print(a*b/c)

I. Write a program that prints the length of user's full name.

full_name = input("Please enter your full name:")

full_name_length = len(full_name)

print(full_name_length)


J. Write a program that asks user for some Float number. This program
soon will round this float number. Additionally, we need to ask for
how many decimal digits user want to round it to. Print its rounded
value.

float_number = float(input("Enter any float number:))

decimal_digits = int(input("Enter how many digits you want to round float number:))

rounded_float_number = round(float_number,decimal_digits)

print(rounded_float_number)

K. Write a program that asks for 2 numbers. 1st number is the main
number, and the 2nd number is for the power the user wants the 1st
number to raise to. So if the 1st number is 16, and the 2nd is 2,
we should see 256 on the console.

first_number = int(input("enter first number:"))

second_number = int(input"enter the power you want the 1st number to raise:")

result = first_number ** second_number

print(result)

L. Write a program that asks user for any single word. Then ask for
any number, because we will call String's 'center' method and give
it the number user inputted.

single_word = input("Enter any single word:")

any_number = input("Enter any number:")

result = single_word.center(any_number)




M. Write a program that asks 'How many times should the program
type "Python" word?'. Print the 'Python' word given number times.
For example, if user gives us the 5 number, we should see on console:
PythonPythonPythonPythonPython

print("How many times should the program type \"Python\" word?")

number = int(input("enter the number:"))

print("Python" * number)


N. Write a program that asks user for any sentence. The program should
replace all characters in the sentence with its capitalized form.
Given "I love the Python", the program should give us:
I LOVE THE PYTHON

sentence = input("Enter any sentence:")

new_sentence = sentence.upper()

print(new_sentence)

O. Write a program that asks user for any sentence. The program should
replace all 'a' character in the sentence with 'o'. Given "Today is a
great day!", the program should give us:
Todoy is o greot doy!

sentence = input("Enter any sentence:")

new_sentence = sentence.replace("a","o")

print(new_sentence)

P. Write a program that asks user for any input. The program should
print 'True' if all characters in the input are lower characters.

sentence = input("Enter any sentence:")

print(sentence.islower())

Q. Write a program that asks user for any input. The program should
print 'True' if all characters in the input are digits.

sentence = input("Enter any sentence:")

print(sentence.isdigit())

R. Write a program that asks user for any phrase. The program should also
ask for the amount the phrase will be printed. Depending on that amount print
the user's phrase to terminal output.

any_phrase = input("Enter any phrase you want:")

number = input("Enter the amount the phrase will be printed:")

print(any_phrase * number)


S. Write a program that asks user for any amount. Depending on that amount you
should print the stars before and after the 'Hello world' phrase. Example:
(Amount is 3)
*** Hello world ***

phrase = "Hello World"

amount = int(input("Enter any amount please:"))

stars = ("*") * amount

print(f"{stars} Hello World {stars}")


OR another method:

phrase = "Hello World"

new_phrase = phrase.center(17,"*")

print(new_phrase)


- Chat GPT's Homework -
Task 1. Create a Python program that greets the user and asks for their name. 
Use the input() function to receive the user's input and then print a personalized greeting.

name = input("Enter your name,please:")

print(f"Welcome,{name}!")

Task 2. Extend the program from Task 1 to ask the user for their birth year and 
calculate their age. Display a message that includes their name and age.

name = input("Enter your name,please:")

birth_year = int(input("Enter your birth year,please:"))

age = 2023 - birth_year

print(f"Hello,{name}.You're just {age} years old.You're young")


Task 3. Write a program that takes two numbers as input from the user and performs 
the following math operations:
A. Addition
B. Subtraction
C. Multiplication
D. Division

first_number = float(input("Enter first number:"))

second_number = float(input("Enter second number:"))

print(first_number + second_number)

print(first_number - second_number)

print(first_number * second_number)

print(first_number // second_number)

Task 4. Create a program that calculates the area of a triangle.
Ask the user for the necessary inputs for calculations. 

AB = float(input("Enter the length of the base of triangle:"))

AC = float(input("Enter the length of the height of triangle:"))

S = 1/2 * AB * AC

print(S)

Task 5. Create a program that calculates the area of a rectangle.
Ask the user for the necessary inputs for calculations. 

AB = float(input("Enter the length of rectangle:"))

AC = float(input("Enter the width of rectangle:"))

S = AB * AC

print(S)

Task 6. Create a program that calculates the area of a square.
Ask the user for the necessary inputs for calculations. 

from math import PI

Radius = float(input("Enter the radius of the square:"))

S = PI ** R

print(S)

Task 7 (Extra!). For an extra challenge, implement a unit conversion feature. 
Ask the user for a distance in meters and convert it to feet and inches. 
There are approximately 3.28084 feet in a meter and 39.3701 inches in a meter. 
Display the converted distances.

distance_in_meters = float(input("Enter the distance in meters, please:"))

distance_in_feets = distance_in_meters * 3.28084 

print(distance_in_feets)

Quiz:
1. Which of the following functions is used to convert a value to an integer in Python?
    a) int()
   

2. When using the input() function in Python, what data type is the input value 
stored as by default?
    
    c) str
    

3. You want to find out how many characters are in a user-inputted sentence. 
Which Python function would you use?
    
    c) len()
    

4. If a user enters "3.14159" as input using the input() function, how can you 
convert it to a floating-point number?
    a) float(input())
  

5. If a user enters "5.7" as input using the input() function and you use 
int(input()) for conversion, what will happen?
    a) An error will occur since int() cannot handle decimal values.
    

6. You want to display the length of a user-inputted string "Hello, World!" with a 
descriptive message. Which option achieves this?
    a) print("The length of the input is:", len(input()))
   

7. What happens if a user enters "42" as input and you use float(input()) for 
conversion?
    
    b) The value is converted to the floating-point number 42.0.
   

8. To style the user prompt and concatenate it with a variable, which option is correct?
    a) input("Enter your name: " + name)
   
"""
