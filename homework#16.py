"""
- While Loops -
A. Write a program that asks user for a number between 100 and 500. The program should ask the user
until he/she enters the number within a given range.

number = int(input("Enter number between 100 and 500:"))
number = 0
while number < 100 or number > 500:
    number = int(input("Enter number between 100 and 500:"))
else:
    print("OK")

B. Write a program that prints even and odd numbers between 1 to the entered number.

number = int(input("Enter number:"))
a = 1
while a <= number:
    if a % 2 == 0:
        print(f"Even number: {a}")
    else:
        print(f"Odd number :{a}")
    a = a + 1


C. Write a program to display each character from a string and if a 
character is number then stop the loop.

input_string = input("Enter any sentence:")
index = 0
while index < len(input_string):
    current_char = input_string[index]
    if current_char.isdigit():
        break
    print(current_char)
    index += 1

D. Write a program to calculate the sum of series up to n term. For example, 
if n=5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

summ = 0
n = 0
while n < 5:
    summ = summ + int(str(2) * (n+1))
    n = n + 1
    print(summ)


E. Create a program that prompts the user to enter a number, 
then use a while loop to count from 1 up to the user's number.

number = int(input("Enter the number:"))
n = 1
while n <= number:
    print(n)
    n+=1


F. Write a Python program that uses a while loop to print numbers from 1 to 10.

n = 1
while n <= 10:
    print(n)
    n+=1


G. Write a program that checks if a user-entered string is a palindrome (reads the same forwards 
and backwards) using a while loop. Ignore spaces and letter case.

sentence = input("Enter the sentence:").lower().strip()
while sentence == sentence[::-1]:
    print("Palindrom")
    break
else:
    print("NO")


H. Write a program that asks the user for an integer. If the number is even, divide it by 2, 
if it's odd, multiply it by 3 and add 1. Repeat this process with the result until the result 
becomes 1, and count how many steps it took.


n = int(input("Enter the number:"))
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    count += 1
print(count)



I. Create a program that calculates the sum of all even numbers from 1 to a user-specified 
number using a while loop.

upper_limit = int(input("Enter a number: "))
sum_of_even_numbers = 0
current_number = 2
while current_number <= upper_limit:
    sum_of_even_numbers += current_number
    current_number += 2
print(sum_of_even_numbers)


J. Create a program that takes a list of numbers as input and reverses the list using a while loop. 
Do this without using any built-in list reversal methods.

numbers = input("Enter numbers, separate them by space button:").split()
numbers_list = [int(a) for a in numbers]
reversed_list = []
index = len(numbers_list) - 1
while index >= 0:
    reversed_list.append(numbers_list[index])
    index-=1
print(reversed_list)

- Extra Hard -
Task A. Count the total number of digits in a number. If user enters 547,
the program should add each digit, so the output is 16 (as 5 + 4 + 7 = 16).


number = int(input("Enter the number:"))
digit_count = 0
digit_sum = 0
while number > 0:
    digit = number % 10
    digit_count += 1
    digit_sum += digit
    number //= 10

print("Total digits:", digit_count)
print("Sum of digits:", digit_sum)

Task B. Write a program to display all prime numbers within a range.

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
primes = []
current_num = start_range
while current_num <= end_range:
    for i in range(2, current_num):
        if current_num % i != 0:
            primes.append(current_num)
        current_num += 1
        break
print(primes)

Task C. Create a program that takes a string as input and uses a while loop to reverse 
and print the characters of the string.

sentence = input("Enter any sentence:")
reversed_sentence = ""
length = len(sentence)
index = length - 1
while index >= 0:
    reversed_sentence = reversed_sentence + sentence[index]
    index -=1
print(reversed_sentence)


Task D. Write a program that checks if a user-entered string is a palindrome (reads the 
same forwards and backwards) using a while loop. Ignore spaces and letter case.

sentence = input("Enter any sentence:").lower().strip()
while sentence == sentence[::-1]:
    print("palindrom")
    break
else:
    print("Not Palindrom")


Task E. Develop a program that takes an integer as input and prints a number pyramid using a 
while loop. For example, if the user enters 5, the program should print:
    1
   121
  12321
 1234321
123454321

n = int(input("Enter an integer: "))
row_number = n

while row_number > 0:
    row = ""
    for i in range(row_number):
        row += str(n)
        n -= 1

    print(row)
    row_number -= 1

- Chat GPT's Homework -
Task 1: Countdown Timer
Write a program that uses a while loop to create a countdown timer. 
Ask the user to enter a number of seconds, and then display a countdown 
from that number down to 0.

seconds = int(input("Enter the number of seconds for the countdown: "))
current_seconds = seconds
while current_seconds > 0:
    current_seconds -= 1
    print(f"{current_seconds} seconds remaining")

Task 2: Number Guessing Game
Create a number guessing game where the computer generates a random number, 
and the user has to guess it. Use a while loop to allow the user to keep 
guessing until they correctly guess the number.

import random
number_to_guess = random.randint(1, 100)
user_guess = 0
while user_guess != number_to_guess:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")

Task 3: Factorial Calculator
Write a program that calculates the factorial of a given number using a while 
loop. Ask the user for an integer input and compute its factorial.

num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("The factorial is:", factorial)

Task 4: Password Validation
Implement a program that asks the user to enter a password. Use a while loop 
to keep asking for the password until it matches a predefined correct password.

correct_password = "QWERTY"
user_password = 0
while user_password != correct_password:
    user_password = input("Enter password:")
else:
    print("Match")


Task 6: Sum of Even Numbers
Calculate and display the sum of all even numbers from 1 to a user-defined 
upper limit using a while loop.

upper_limit = int(input("Enter the upper limit:"))
sum = 0
i = 1
while i < upper_limit:
    i += 1
    if i % 2 == 0:
        sum += i
print(sum)



Task 7: Multiplication Table
Generate and display the multiplication table for a given number using a while 
loop. Ask the user for the number and the range (e.g., 1 to 10).


num = int(input("Enter number:"))
start = int(input("Enter the start number:"))
stop = int(input("Enter the stop number:"))
i = 1
while i <= stop:
    mult = num * i
    i+=1
    print(mult)

    

Task 8: Pattern Printing
Write a program that uses a while loop to print a pattern of asterisks, 
where the number of asterisks on each line is equal to the line number. 
For example:
*
**
***
****
*****

row = int(input("Enter the rows number:"))
i = 1
while i <= row:
    print("*" * i)
    i+=1

Task 9: Task with a for loop
Create a program that uses both while and for loops. Ask the user for a number 
and print its multiplication table using a for loop inside the while loop. 
Continue asking for numbers until the user enters '0' to exit.

while True:
   number = int(input("Enter number:"))
   if number == 0:
       break
   for i in range(1,11):
       mult = number * i
       i+=1
       print(mult)

Quiz.
1. What is the primary purpose of a while loop in Python?
    a) To execute a block of code a specific number of times.


2. What are some best practices for using while loops in Python?
    a) Always initialize loop control variables within the loop.
 
3. What should you consider when using a while loop in Python?
    a) Potential performance impact.
    

4. What are the key differences between while and for loops in Python?
    a) While loops are primarily used for iteration, while for loops are used 
    for conditional execution.
    
5. What is the potential risk of using an infinite while loop in your code?
    
    b) It can lead to unexpected program termination.
  

6. How do you ensure that a while loop will terminate and not result in an infinite loop?
    
    c) By ensuring the loop condition becomes false at some point.
    

7. Which of the following statements is true about the loop control variable in a while loop?
  .
    c) It is used to define the loop condition and manage loop execution.
    

8. In Python, what happens when the condition of a while loop is initially False?
    a) The loop is skipped entirely, and the code continues after the loop.


9. What is an off-by-one error in the context of while loops?
   
    b) An error that happens when a loop runs one more or one less time than intended.
  

10. What is the output of the following code?
    count = 1
    while count <= 5:
        print(count)
        count += 1

    a) 1 2 3 4 5


11. What is the output of the following code?
    while True:
        print("Infinite Loop")

    a) Infinite Loop


12. What is the output of the following code?
    count = 1
    while count <= 10:
        if count == 5:
            break
        print(count)
        count += 1

    
    b) 1 2 3 4
   

13. What is the output of the following code?
    count = 1
    while count <= 5:
        if count % 2 == 0:
            count += 1
            continue
        print(count)
        count += 1

    
    b) 1 3 5
   

14. What is the output of the following code?
    outer_count = 1
    while outer_count <= 3:
        inner_count = 1
        while inner_count <= 2:
            print(outer_count, inner_count)
            inner_count += 1
        outer_count += 1

    a) 1 1 2 1 3 1
    b) 1 1 2 1 3 2
    c) 1 2 2 2 3 1
    d) 1 2 2 1 3 2
    e) None of the above

15. What is the output of the following code?
    num = 5
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    print(fact)

    a) 120
  
16. What is the output of the following code?
    total = 0
    while True:
        num = int(input("Enter a number (0 to exit): "))
        if num == 0:
            break
        total += num
    print("Sum:", total)

    a) The program adds numbers until the user enters 0 and then displays the sum.
 .

17. What is the value of x:
    x = 0
    while (x < 100):
        x += 2
        print(x)

   
    d) 100

18. What is the output of the following if statement
    a, b = 12, 5
    if a + b:
        print('True')
    else:
        print('False')

    
    b) True

19. What is the value of the var after the for loop completes its execution:
    var = 10
    for i in range(10):
        for j in range(2, 10, 1):
            if var % 2 == 0:
                continue
                var += 1
        var+=1
    else:
        var+=1

    b) 21
    

20. What is the output of the following nested loop:
    for num in range(10, 14):
        for i in range(2, num):
            if num%i == 1:
                print(num)
                break

    a)
    10
    11
    12
    13
 

21. What is the output of the following nested loop:
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
    
"""