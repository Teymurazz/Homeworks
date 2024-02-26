"""
- For Loops -
A. Write a program to use the loop to find the factorial of a given number.

factorial = 1
number = int(input("Enter the number :"))
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)


B. Write a program that uses a for loop to print numbers from 1 to 10. However, 
if the number is divisible by 3, skip the loop, and if the number is 7, stop the loop.

for i in range(1, 11):
    if i == 3:
        continue
    elif i ==7:
        break
    print(i)

C. In Python, what is the purpose of the range() function when used with a for loop?

to cycle inside the given number range

D. How can you prematurely exit a for loop in Python?

with break option

E. What is an iterator in Python, and how is it related to for loops?

An iterator in Python is an object that represents a collection of elements 

and allows you to iterate over them one by one

F. How can you iterate through the elements of a list in reverse order using a for loop?

for number in reversed_numbers:
    print(number)

G. Create a for loop that prints all even numbers from 20 to 40. Solve this task in
two different ways (modifying range() and using if-statements).

for i in range(20, 41):
    if i % 2 == 0:
        print(i)


H. Write a for loop to calculate the sum of all integers from 1 to 100. At the end of the loop 
the program should print 'The end of a task.'

summ = 0
for i in range(1, 101):
    summ+=i
print(summ)
print("The end of a task")


I. Generate a multiplication table for a given number using a for loop, e.g., for the number 5, print 5x1, 5x2, ..., 5x10.

number = 5
for i in range(1,11):
    mult = number * i
    print(f"{number} * {i}  = {mult}")


J. Write a for loop to iterate through a string and print each character on a separate line
with corresponding index.

sentence = "Hello World"
for char, index in enumerate(sentence, start = 0):
    print(char, index)


K. Suppose you have the following list:
employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]

Iterate over this list and print all names except the ones which start with the
letter 'J'.

employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]
for names in employees:
    if names.startswith("J"):
        continue
    print(names)

L. Suppose you have the following list:
stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]

Iterate over this list and print all fruits and vegetables except the ones which start with the
letter 'C' and whichs length is less than or equal 6.

stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]
for fruits in stock:
    if fruits.startswith("C") and len(fruits) <= 6:
        continue
    print(fruits)


M. Write a for loop to reverse a given string. For example, "hello" should become 'olleh'.
You shouldn't use any reversing methods such as [::-1]. Instead you should make manipulations
with string literals.

sentence = "Hello"
reversed_sentence = ""
for i in sentence:
    reversed_sentence = i + reversed_sentence
print(reversed_sentence)
    
N. Write a for loop to check and print all prime numbers within a given range (on dynamic user input).

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in range(start, end+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)



O. Implement a for loop to search for a specific word in a text and replace it with another word.

text = "This is a sample text with specific word"
search_word = "specific"
new_word = "new"
words = text.split()
for i in range(len(words)):
    if words[i] == search_word:
        words[i] = new_word
new_text = " ".join(words)
print(new_text)

P. Write a program that draws the pyramid as:
Reverse Pyramid
  ***********     
   **********
    ******
     *****
      ***
       *

rows = 6
for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


Q. Write the shortest program that prints the position and each character of a string.

sentence = input("<<")
from collections import Counter
char_counts = Counter(sentence)
print(char_counts)        


R. You have the following dictionary:
data = {
    "key1": 80,
    "key2": 75,
    "key3": 65,
    "key4": 85
}

Iterate over it and check if any value is less than 80, add the missing points.

data = {
    "key1": 80,
    "key2": 75,
    "key3": 65,
    "key4": 85
}
for key, value in data.items():
    if value < 80:
        data[key] = value + (80 - value)
print(data)

or

for key, value in data.items():
    if value < 80:
       data[key] = 80
print(data)


S. Copy this code to your file:
from random import randint
numbers = [randint(15, 40) for _ in range(5)]

This gives you a list of 5 random numbers between 15 and 40. Using for loops
find the max value of that list, and print the list to see values.

from random import randint
numbers = [randint(15, 40) for _ in range(5)]
for num in numbers:
    print(max(numbers))
print(numbers)


T. Use 'numbers' list from Task S. Iterate over it again, and if there is a number
between 20 and 25 exit the loop, otherwise print the value.

from random import randint
numbers = [randint(15, 40) for _ in range(5)]
for num in numbers:
    if num > 20 and num < 25:
        break
    else:
        print(num)

        
U. Write a Python program to construct the following pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

for i in range(6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)


V. Write a Python program to count the number of even and odd numbers in a collection of numbers.

numbers = [2, 3, 4, 5, 8, 9, 11, 15, 22]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
print(f"the number of even numbers is {even}")
print(f"the number of odd numbers is {odd}")


W. Write a Python program that prints each item and its corresponding type from the following list.
[5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]

for item in lst:
    print(item, type(item))


X. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    print(i)


Y. Write a Python program that accepts a string and calculates the number of digits and letters.

sentence = input("Enter any sentence:").strip()
letters = 0
digits = 0
for i in sentence:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
print(f"the number of letters is {letters}")
print(f"the number of digits is {digits}")


Z. Write a Python program to guess a number between 1 and 9. The program should use 'random' module,
give only 3 chances to guess the number. Print 'Congratulations' if you guess and 'Game Over'
if you fail.

import random

comp_choice = random.randint(1, 10)
print("You have 3 attempts")
for i in range(3):
    guess = int(input(f"{i+1} attempt. Enter the number:"))
if comp_choice == guess:
     print("Congratulations")
else:
     print("Fail")
print(f"Computer choice was {comp_choice}")

- Chat GPT's Homework -
Problem 1: Generate a Series
Write a Python program that uses a for loop to generate and print the following 
series of numbers: 1, 4, 9, 16, 25, ... up to a given positive integer n. The 
series consists of perfect squares.

n = int(input("Enter the number:"))
lst = [i **2 for i in range(1, n+1)]
print(lst)

Problem 2: Calculate Factorial with a For Loop
Write a Python program that calculates the factorial of a given positive integer n 
using a for loop. Display the result.

n = int(input("Enter the number:"))
factorial = 1
for i in range(1, n+1):
    factorial*=i
print(factorial)

Problem 3: Password Generator
Write a Python program that generates a random password consisting of both uppercase 
and lowercase letters, digits, and special characters. The password should be of a 
specified length n. Use a for loop to create the password.

import string
import secrets

letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*(){}"
char = letters + digits + symbols
length = int(input("Enter the length of pass:"))
password = [secrets.choice(char) for _ in range(length)]
result_pass = "".join(password)
print(result_pass)


Problem 4: Average of Numbers
Write a Python program that calculates the average of a list of numbers using a 
for loop. Prompt the user to enter a list of numbers (comma-separated), and then 
compute and display the average.

lst = input("Enter the numbers and separate them by comma:").split(",")
number_list = [int(a) for a in lst]
summ = sum(number_list)
length = len(number_list)
average = summ / length
print(average)


Problem 5: Pattern Printing
Write a Python program that prints the following pattern using nested for loops:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

row = 5
for x in range(1, row+1):
    for y in range(1, x + 1):
        print(y,end="")
    print()

Problem 6: Count Vowels and Consonants
Write a Python program that counts the number of vowels and consonants in a given 
string. Use a for loop to iterate through the characters of the string and 
categorize them as vowels or consonants. Display the counts separately.

sentence = "Hello World"
without_space = sentence.replace(" ", "")
vowels_num = 0
consonants_num = 0
vowels = ["a","i","o","u","e"]
for i in without_space:
    if i in vowels:
        vowels_num+=1
    else:
        consonants_num+=1
print(f"the number of vowels is {vowels_num}")
print(f"the number of consonats is {consonants_num}")


or

string = input("Enter the string:")
vowels = ["a", "e", "i", "u", "o"]
vowels_count = 0
consonant_count = 0
for char in string:
    if char.isalpha():
        if char in vowels:
           vowels_count+=1
        else:
            consonant_count+=1
print(vowels_count)
print(consonant_count)

Problem 7: Reverse a List
Write a Python program that takes a list as input and uses a for loop to reverse 
the order of elements in the list. Display the reversed list.

lst = [input("<<") for i in range(5)]
print(lst)
input_lst = lst[::-1]
output_lst = []
for i in input_lst:
    output_lst.append(i)
print(output_lst)


Problem 8: Finding Factors
Write a Python program that prompts the user to enter a positive integer and 
then finds and prints all the factors of that integer using a for loop.

fact = 1
number = int(input("Enter the number"))
for i in range(1, number + 1):
    fact*=i
print(fact)


Quiz.
1. How do you terminate a 'for' loop prematurely in Python?
    a) Using 'break'
   '

2. What is the syntax for a 'for' loop in Python?",

    b. for i in range(5)
    

3. Which statement is used to skip the current iteration and continue to the next 
in a 'for' loop?
    
    c) 'continue'

4. What is the maximum number of times a 'for' loop can iterate?",
    
    d) There is no maximum limit

5. Which data types can be iterated over using a 'for' loop in Python?
    
    b) Lists and dictionaries
    

6. In a 'for' loop, how can you access both the index and value of each element in a list?

    b) Use the enumerate() function

"""