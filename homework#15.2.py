"""
- For Loops -
A. Write a Python program that uses a for loop to print 
all even numbers from 1 to 20, inclusive. Use the continue 
statement to skip odd numbers during the iteration.

for i in range(1,21):
    if i % 2 != 0:
        continue
    print(i)

B. Write a Python program that asks the user to input 10 numbers. 
Use a for loop to iterate through the numbers. Print the sum of 
all numbers entered by the user. Use the break statement to exit 
the loop early if the user inputs a negative number.

sum_of_numbers = 0
for i in range(1, 11):
    user_input = int(input("Enter number:"))
    if user_input < 0:
        break
    sum_of_numbers += user_input
print(sum_of_numbers)

C. Write a Python program that takes an integer as input from 
the user and prints its multiplication table up to 10 using a for loop. 
Use the continue statement to skip the multiplication if the result 
is less than 30.

number = int(input("Enter the number:"))
for i in range(1,11):
    mult = number * i
    if mult < 30:
        continue
    print(mult)

D. Write a Python program to find and print all prime numbers between 
1 and 50 using a for loop. Use the break statement to exit the loop 
early if a non-prime number is encountered.

for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

E. Write a Python program to generate and print the first 10 numbers 
in the Fibonacci sequence using a for loop. Use the continue statement 
to skip printing a number if it is greater than 100.

a, b = 0, 1
for i in range(11):
    print(a, end ="")
    a, b = b, a + b

F. Write a Python program that asks the user to input an integer n. 
Using a for loop, print all even numbers in reverse order from n down 
to 2. Use the continue statement to skip odd numbers during the iteration.

number = int(input("Enter the number:"))
for num in range(number, 1 , -1):
    if num % 2 !=0:
        continue
    print(num)


G. Write a Python program that prompts the user for a password. Use a for 
loop to iterate over a predefined list of passwords. If the entered password 
matches any of the predefined passwords, print "Access granted" and use the 
break statement to exit the loop. If no match is found, print "Access denied".

valid_passwords = ["password1", "password2", "password3"]
user_password = input("Enter your password: ")
for password in valid_passwords:
    if user_password == password:
        print("Access granted")
        break
    else:
        print("Access denied")

or

valid_passwords = ["password1", "password2", "password3"]
user_input = input("Enter your password:")
if user_input in valid_passwords:
    print("Access granted")
else:
    print("Access denied")


H. Write a Python program that asks the user to enter a series of numbers. 
Use a for loop to iterate through the numbers. Compute and print the average 
of all positive numbers entered by the user. Use the continue statement 
to skip negative numbers during the calculation.

numbers = input("Enter numbers:").split()
positive = []
numbers_list = [int(a) for a in numbers]
for num in numbers_list:
    if num < 0:
        continue
    positive.append(num)
print(sum(positive) / len(positive))

I. Write a Python program that prompts the user to input a sentence. 
Use a for loop to iterate through the characters in the sentence and count 
the number of vowels (a, e, i, o, u). Print the total count of vowels. 
Use the continue statement to skip counting for non-alphabetic characters.

sentence = input("Enter a sentence: ")
vowel_count = 0
for char in sentence:
    if char.isalpha():
        char = char.lower()
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    else:
        continue
print("Total count of vowels:", vowel_count)

J. Write a Python program that generates a random password of a specified 
length based on user input. Ask the user to input the desired password 
length and use a for loop to generate and print the password. Use the 
break statement to exit the loop after generating the password.

import random
import string
password_length = int(input("Enter the desired password length: "))
generated_password = ''
for _ in range(password_length):
    random_char = random.choice(string.ascii_letters + string.digits)
    generated_password += random_char
print("Generated Password:", generated_password)


K. Write a Python program that prompts the user to enter the names of 
three cities and their corresponding populations. Use a for loop to populate 
a dictionary where the city names are keys and the populations are values.

cities = []
populations = []

for i in range(3):
    city = input("Enter the name of the city: ")
    city_population = int(input("Enter the population of the city: "))

    cities.append(city)
    populations.append(city_population)

cities_dict = dict(zip(cities, populations))

print(cities_dict)

L. Write a Python program that asks the user to input a sentence. Use a for 
loop to iterate through the characters in the sentence and count the number 
of vowels (a, e, i, o, u). Store the counts in a dictionary where the vowels 
are keys and the counts are values.

vowel_count = {}

sentence = input("Enter a sentence: ")

for char in sentence:
    if char.lower() in "aeiou":
        if char not in vowel_count:
            vowel_count[char] = 1
        else:
            vowel_count[char] += 1
print(vowel_count)


M. Write a Python program that allows the user to enter key-value pairs into 
a dictionary. Prompt the user to input a key and a value, and use a for loop 
to allow them to enter multiple pairs. Print the dictionary after each addition.

dictionary = {}
for _ in range(int(input("How many key-value pairs do you want to add? "))):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dictionary[key] = value
print("The dictionary after each addition is:")
print(dictionary)


N. Write a Python program that prompts the user to input a word or phrase. 
Use a for loop to iterate through the characters and count the frequency of 
each letter in the input. Store the counts in a dictionary where the letters 
are keys and the counts are values.

input_word = input("Enter a word or phrase: ")
letter_count = {}
for letter in input_word:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
for letter, count in letter_count.items():
    print(f"The letter '{letter}' appears {count} time(s) in the input.")


    or


dict = {}
sentence = input("Enter sentence:")
for letter in sentence:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] +=1
print(dict)


O. Write a program to use for loop to print the following reverse number pattern:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1


for x in range(5, 0, -1):
    for y in range(x, 0, -1):
       print(y,end = "")
    print()
    

P. Display numbers from -10 to -1 using for loop. The step of your range
method should be positive, not negative. The output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

for i in range(-10, 0, 1):
    print(i)

- EXTRA HARD -
Task 1.
Count the total number of digits in a number.
Write a program to count the sum of digits in a number.
For example, the number is 75869, so the output should be 35 (7 + 5 + 8 + 6 + 9).


number = int(input("Enter the number:"))
summ = 0
str_number = str(number)
count_of_digits = len(str_number)
for i in range(len(str_number)):
    summ = summ + (int(str_number[i]))
print(summ)
print(f"There are {count_of_digits} digits in number")


Task 2.
Write a program to calculate the sum of series up to n term. 
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

summ = 0
x = 5
for i in range(5):
    summ = summ + int(str(2) * (i+1))
print(summ)


Task 3.
Write a program to display whether the number is prime or not.
Prime numbers are natural numbers that are divisible by only 1 and the number itself.

a = int(input("enter number: "))
k = 0
for i in range(2, a):
    if a % i == 0:
        k = k+1
if (k == 0):
    print("This is prime number")
else:
    print("This is not prime number")

- Chat GPT's Project -
Project: Password Validation

Write a Python program that prompts the user to enter a password. The program 
should check the validity of the password based on the following conditions:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter, one lowercase letter, 
and one numeric digit.
The password must not contain the word "password" (case insensitive).
Use a for loop to iterate through the characters of the password and implement 
the following actions:

If the current character is a space, use continue to skip the rest of the loop 
and move to the next character.
If the password contains the word "password" (case insensitive), use break to 
immediately exit the loop and print "Invalid password".
After the loop, check if the password meets all the conditions. If it does, 
print "Valid password". Otherwise, print "Invalid password".
Ensure that the program provides appropriate messages to guide the user and 
thoroughly tests the input for validity.

This task challenges the usage of for loops, break, and continue to handle 
complex conditions and ensure secure password validation. Happy coding!

Quiz.
1. What is the purpose of the continue statement in a for loop?

    d) It checks if the loop condition is met.

2. In a for loop, the break statement is used to:

    b) Exit the loop and move to the next block of code.
 

3. Which of the following statements is true about the for loop in Python?

    b) The loop variable can be of any data type.
  

4. For the following code snippet, determine the output or the result of the operation:
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        else:
            continue
    print(total)

    6

5. For the following code snippet, determine the output or the result of the operation:
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for num in numbers:
        if num > 30:
            break
        if num % 2 == 0:
            total += num
        else:
            continue
    print(total)

    60

6. What is the value of the var after the for loop completes its execution:
    var = 10
    for i in range(10):
        for j in range(2, 10, 1):
            if var % 2 == 0:
                continue
                var += 1
        var += 1
    else:
        var += 1
    print(var)

    
    b) 21
    

7. What is the output of the following range() function:
    for num in range(2,-5,-1):
        print(num, end=", ")

    c) 2, 1, 0, -1, -2, -3, -4

8. What is the value of x after the following nested for loop completes its execution:
    x = 0
    for i in range(10):
        for j in range(-1, -10, -1):
            x += 1
            print(x)
    
    
    b) 90
  

9. What is the output of the following nested loop?
    for num in range(10, 14):
        for i in range(2, num):
            if num % i == 1:
                print(num)
                break

10
11
12
13
                
10. What is the output of the following nested loop?
    numbers = [10, 20]
    items = ["Chair", "Table"]

    for x in numbers:
        for y in items:
            print(x, y)
        
    a)
    10 Chair
    10 Table
    20 Chair
    20 Table
 

11. What is the output of the following loop?
    for l in 'Jhon':
        if l == 'o':
            pass
        print(l, end=", ")
            
    
    b) J, h, o, n,

- True or False -
True or False: A for loop in Python can be nested within another for loop.   True
True or False: The continue statement is used to immediately exit the loop
and terminate the program.  False
True or False: The break statement is used to exit the loop prematurely, 
regardless of whether the loop condition is met. False
True or False: The break statement is used to skip the rest of the loop and 
move to the next iteration. True
True or False: The continue statement is used to exit the loop prematurely, 
regardless of whether the loop condition is met. False
True or False: Using break is more appropriate when you want to exit the 
loop prematurely based on a certain condition, regardless of whether the 
loop has completed all iterations. It allows you to terminate the loop early 
and continue with the rest of the program.  True
True or False: Using continue is more appropriate when you want to skip the 
current iteration and proceed to the next iteration based on a certain condition, 
but you still want to continue the loop.  True
"""