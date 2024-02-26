"""
Instructions. Write Python programs to solve the following tasks,focusing 
on error handling using try and except blocks. In each program, you should 
handle potential errors gracefully and provide appropriate error messages.

- Error Handling -
A. Divide by Zero:
Write a program that takes two numbers as input from the user and 
calculates their division result. Handle the ZeroDivisionError exception 
that might occur if the user attempts to divide by zero. Display an error 
message in such cases.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
try:
    c = a / b
except ZeroDivisionError:
    print("It's prohibited divide to zero")
else:
    print(c)

B. File Reading:
Write a program that reads the content of a file specified by the 
user. Handle the FileNotFoundError exception if the file does not exist, 
and display an error message. If the file exists, display its content.

try:
    with open("document.txt") as file:
        file.read()
except FileNotFoundError:
    print("This file is not exist")

C. List Element Access:
Create a list with some elements, and then write a program that asks the 
user for an index to access an element from the list. Handle the IndexError 
exception if the user provides an index that is out of bounds and display an error message.

lst = ["Aysel", "Gunel", "Asif", "Murad"]
try:
    index = int(input("Enter the index of student which info you are interested:"))
    print(f"The index {index} is belong to {lst[index]} student")
except IndexError:
    print("The index is out of range")

D. Dictionary Key Access:
Create a dictionary with some key-value pairs. Write a program that prompts the
user for a key and attempts to access the corresponding value. Handle the 
KeyError exception if the user enters a key that does not exist in the 
dictionary and display an error message.

info = {
    "Mark": 22,
    "John": 45,
    "Tom": 19
}
try:
    name = input("Enter the name of a person whici info you want:")
    print(f"the age of the person under the {name} name is {info[name]}")
except KeyError:
    print("Error. This key doesn't exist in the dictionary")

E. Word Counter:
Write a program that reads the content of a text file specified by the user 
and counts the number of words in it. Handle the FileNotFoundError exception if the 
file does not exist and display an error message.

try:
    with open("document.txt") as file:
        file.read()
except FileNotFoundError:
    print("This file is not exist")

F. Module Import:
Write a program that tries to import 'django' module. Handle the occuring exception 
if the module does not exist and display an error message.

try:
    import django
    print("Django module imported successfully")
except ImportError:
    print("Error: Django module not found")


G. User Input:
Write a program that uses infinite loop and prompts the user until he/she inputs an integer.
When the input is given properly, the loop should be exited and the program should print 'Exiting'.

while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print("Exiting")
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

Quiz.
1. What is error handling in programming?
   
    c) A mechanism to gracefully deal with unexpected issues and exceptions
    

2. Which Python keyword is used to catch exceptions in a try-except block?
 
    c) except
    
    
3. What will the following Python code snippet output?
    try:
        num = 10 / 0
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    a) Division by zero is not allowed.
  

4. What is the purpose of the finally block in a try-except-finally structure?
   
    c) It always executes, regardless of whether an exception is raised or not.
   

5. In Python, which of the following statements is true about exceptions?
   .
    c) Multiple except blocks can be used to catch different exceptions.
 

6. What is the primary purpose of raising a custom exception in Python?
    
    d) To ignore errors and continue program execution.

7. Which of the following statements is true about the else block in a try-except-else structure?
   
    b) It executes only if no exception is raised.
  

8. What is the output of the following Python code snippet?
    try:
        x = int("abc")
    except ValueError as e:
        print(e)

    c) invalid literal for int() with base 10: 'abc'
   

9. Which error handling approach allows you to specify different code blocks for different exceptions?
    a) try-except


10. When using the with statement to open a file, what does it ensure regarding the file's state?
    a) It guarantees that the file will be closed when the block is exited, even if an exception occurs.
    b) It automatically handles all exceptions that may occur during file operations.
    c) It ensures that the file is locked for exclusive access during the block execution.
    d) It prevents the file from being modified during the block execution.

11. Which of the following is NOT a built-in exception in Python?

    b) CustomException


12. What is the output of the following Python code snippet?
    try:
        x = 5 / 0
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Finally block executed.")

   
    d) "Finally block executed."
    
13. In Python, what does the except keyword allow you to do when handling exceptions?
    a) Specify the type of exception to catch


14. What type of error occurs when a variable is used before it has been assigned a value?

    c) NameError
    

15. In a try-except block, can you have multiple except blocks for the same exception type?
    a) Yes, you can have multiple except blocks for the same exception type.

16. What is the purpose of the else block in a try-except-else structure?

    d) It specifies code to execute if no exception is raised.
"""