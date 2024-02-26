"""
- Decorators -
A. Create a decorator named @my_decorator that simply prints a message 
before and after the decorated function is called.

def my_decorator(func):
    def wrapper():
        print("This is the start of function")
        func()
        print("This is the stop point of function")
    return wrapper

@my_decorator
def example_function():
    print("Hello World")

example_function()


B. Modify the my_decorator from task 1 to accept arguments. The decorator 
should be able to take arguments like a message and print it before and 
after the decorated function is called.

def my_decorator(func):
    def wrapper(message = input("Enter here the message you want to see :")):
        print(message)
        func()
        print(message)
    return wrapper

@my_decorator
def example_function():
    print("Hello World")

example_function()    

C. Create a decorator named @timer that measures the time it takes for a 
decorated function to run. Print the elapsed time in seconds.

import time
def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        result = end - start
        print(f"this function was executed {result} seconds")

    return wrapper

@my_decorator
def greet():
    time.sleep(3)
    print("Hello")

greet()


D. Extend the timer decorator from Task C to accept a parameter specifying 
the time units (e.g., seconds, milliseconds, microseconds) for printing the 
elapsed time.


E. Implement a decorator @log_calls that logs function calls, including 
function name, arguments, and return value.

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"The function name is {func.__name__}")
        print(f"The function parameters are {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"The function return value is {result}")
        return result
    return wrapper

@log_calls
def add_function(a, b):
    return(a * b)

add_function(5, 2)


F. Create multiple decorators and demonstrate how they can be chained to 
decorate a single function.

G. Implement a decorator @check_authentication that checks if a user is 
authenticated before calling the decorated function. If authenticated, 
allow the function to execute; otherwise, print an authentication error message.


H. Write a decorator @argument_decorator that accepts arguments and prints them 
before and after calling the decorated function.

def argument_decorator(func):
    def wrapper(arguments= input("enter arguments you want:")):
        print(arguments)
        func()
        print(arguments)
    return wrapper

@argument_decorator
def greet():
    print("Hello")

greet()

I. Create a decorator @modify_arguments that modifies the arguments passed to the 
decorated function. For example, double all numerical arguments.

def modify_arguments(func):
    def wrapper(*args):
        for arg in args:
            modified_args = arg * 2
        return func(*modified_args)
    return wrapper


@modify_arguments
def add_numbers(a,b):
    print(a, b)

add_numbers(2, 3)


J. Write a decorator @modify_return_value that modifies the return value of the 
decorated function. For example, append a specific string to the return value.

- File Import Handling -
A. Create two Python files, main.py and helper.py. In helper.py, define a function. 
In main.py, import the function from helper.py and use it.
B. Write a Python script that imports a function from another file and executes it 
if the script is run directly. Use if __name__ == "__main__" to control the execution.
C. Extend task 2 by passing arguments to the function imported from another file. 
Demonstrate how the imported function can interact with the arguments provided in the main script.
D. Write a Python script that imports all functions from another module using from module import *. 
Demonstrate the usage of these imported functions.

Quiz.
1. Which of the following is a valid example of a decorator in Python?
    a)
    
    b)
    def my_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper
  
    d)
    def my_decorator():
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper

2. Consider the following decorator and decorated function snippet. 
What does the decorator @my_decorator do when applied to my_function?
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Decorator: Before function call")
            result = func(*args, **kwargs)
            print("Decorator: After function call")
            return result
        return wrapper

    @my_decorator
    def my_function(arg1, arg2):
        print(f"Function called with args: {arg1}, {arg2}")

    my_function("hello", 42)

    a) Prints "Decorator: Before function call", calls the decorated function, 
    prints "Decorator: After function call".
 
  

3. In the context of passing arguments to a decorated function, what does the 
*args parameter in the decorator's wrapper function represent?
    a) It allows passing multiple positional arguments to the decorated function.
   

4. Consider the following Python script. What will be the output if the script is run directly?
    def my_function():
        print("My function in main script")

    if __name__ == "__main__":
        print("Script running directly")
        my_function()

    
    c) My function in main script
    Script running directly
   

5. In the context of using if __name__ == "__main__", why is this construct useful in Python scripts?
    a) It allows the script to define a main function and execute it only when the script is run directly.


6. Consider the following Python script and another script importing it. 
What will be the output when the importing script is run?
    my_module.py:
        def my_function():
            print("My function in my_module")

        if __name__ == "__main__":
            print("Script running directly in my_module")
            my_function()

    main_script.py:
        import my_module

        if __name__ == "__main__":
            print("Script running directly in main_script")
            my_module.my_function()

    d) My function in my_module        
"""