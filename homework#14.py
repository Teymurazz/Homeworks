"""
- For Loops -
A. Write a program that prints "Python" four times in a row.

for x in range(4):
    print("Python")

B. Write a program that prints "Python" four times in one row. Expected output:
PythonPythonPythonPython

for x in range(4):
    print("Python", end="")

C. Write a program that prints numbers from 0 to 7.

for _ in range(8):
    print(_)

D. Write a program that asks the user how many time the phrase should
be printed. Depending on that input the program should print prints the
"Loops are very good" phrase.

count = int(input("Enter how many times you want the phrase printed:"))
for x in range(count):
    print("Loops are very good")

E. Using f-strings and looping five times print the following output:
Looping No.1
Looping No.2
Looping No.3
Looping No.4
Looping No.5

for x in range(5):
    print(f"Looping No.{x+1}")


F. Write a program that asks user for six student name. Add those names
to a list. Then print their name with corresponding order number. Ex. o.:
1. Leyla
2. Aysel
3. Gunel
4. Murad
5. Mark
6. John

student_names = []
for i in range(6):
    name = input("Enter student name: ")
    student_names.append(name)
for index, name in enumerate(student_names, start=1):
    print(f"{index}. {name}")

- Chat GPT's Homework -
1. Write a program that uses a for loop to print the numbers from 1 to 10.

for x in range(1,11):
    print(x)

2. Write a program that calculates and prints the sum of all numbers from 1 to 100 using a for loop.

num = 0
for x in range(1,101):
    num +=x
    print(num)

3. Write a program that takes an integer input from the user and uses a for loop to print the multiplication table for that number up to 10.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

4. Write a program that takes a string input from the user and uses a for loop to count and print the number of characters in the string.

user_input = input("Enter a string: ")
for char in user_input:
    count += 1
print("The number of characters in the string is:", count)

5. Write a program that takes a string input from the user and uses a for loop to print the characters of the string in reverse order.

string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("The reversed string is:", reversed_string)

6. Write a program that takes an integer input from the user and uses a for loop to calculate and print the factorial of that number.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("The factorial of", num, "is", fact)

7. Write a program that takes an integer input from the user and uses a for loop to print a table of powers for that number up to the 5th power.

number = int(input("Enter a number: "))
for i in range(6):
 print(number**i)

Quiz.
1. What is the purpose of loops in programming?
  
    b) To repeat a block of code multiple times
  

2. Which type of loop is commonly used to repeat a block of code a fixed number of times?
   
    b) for loop
 

3. How is the range() function used in a for loop?
  
    c) It defines the number of iterations for the loop
    

4. What's a scenario in real life that can be likened to a loop in programming?
    a) Listening to a song on repeat
  
5. Which of the following code snippets will print "Hello, Loop!" five times?
    a) 
    for i in range(5):
        print("Hello, Loop!")
    b) 
    for i in range(1, 6):
        print("Hello, Loop!")
    

6. What will the following code snippet print?
    for i in range(3):
        print("*" * (i + 1))

    a)
    *
    **
    ***

   
   

7. Loops are essential in programming because they help to:
   
    b) Repeat code without any restrictions
  
    d) Automate repetitive tasks and process collections of data

8. Which of the following options correctly describes an infinite loop?
    
    d) A loop that continues running endlessly

9. What does the range() function return?
    
    b) A sequence of numbers
 

10. Which of the following is NOT an iterable that can be used with a for loop?
    a) Lists
    b) Dictionaries
    c) Strings
    
"""