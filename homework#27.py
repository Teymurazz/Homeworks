"""
- Decorators -
A. Write a decorator function print_decorator that prints a message 
before and after the decorated function is called. The message should 
indicate the start and end of the function call. Apply this decorator 
to a function named example_function that takes no arguments and simply 
prints "Hello, world!".


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

B. Write a decorator function star_decorator that decorates the output 
of the decorated function with a pattern of "*****" before and after the output.
Apply this decorator to a function named example_function that takes 
no arguments and simply returns the string "Hello, Decorators!".

def my_decorator(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper


@my_decorator
def example_function():
    print("Hello decorators")

example_function()


C. Write a decorator function that is used to double the output of the
decorated fucntion.


def my_decorator(func):
    def wrapper(n):
        result = n * 2
        print(result)
        func(n)
    return wrapper

@my_decorator
def main_func(n):
    return n

print(main_func())    


OR

def double_output_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result * 2
    return wrapper_function

@double_output_decorator
def my_function():



Quiz.
1. What is a decorator in Python?
    
    b) A function that takes another function and extends its behavior without modifying the function itself.
 

2. Which symbol is commonly used to denote a decorator in Python?
    a) @
   
    
3. What is the purpose of a decorator?
    a) To modify the behavior of an existing function without modifying the function itself.
    
    
4. Which of the following is a valid use case for decorators?

    c) Adding additional functionality to an existing function.
    

5. In Python, can a function have multiple decorators?
    a) Yes
    
    
6. When using multiple decorators on a function, in which order are they applied?
    
    b) From bottom to top, starting with the innermost decorator.
   

7. Which of the following is true about decorator functions?
    
    d) They can modify the decorated function.
    
8. What is a closure in Python?
    
    b) A nested function that captures and remembers the environment in which it was created.

    
9. Which of the following is a correct way to use a decorator?
    a) @my_decorator
  
10. What will be the output of the code?
    def star_decorator(func):
        def wrapper():
            print("*****")
            func()
            print("*****")
        return wrapper

    @star_decorator
    def greet():
        print("Hello, world!")

    greet()

    a) ***** Hello, world! *****
  

11. What will be the output of the code?
    def repeat_decorator(func):
        def wrapper():
            func()
            func()
        return wrapper

    @repeat_decorator
    def say_hello():
        print("Hello!")

    say_hello()

    a) Hello! Hello!
  
    d) Hello! Hello!
"""