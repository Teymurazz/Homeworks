"""
- Functions -
A. Define a function greet_with_message that takes a username and a 
message (with a default value of "Hello") as parameters and prints 
the message along with the username.

def greet(name):
    print(f"Hello {name}")

greet()


OR


def greet_with_message(name, greet = "Hello"):
     return greet + " " + name

print(greet_with_message(""))



B. Write a function calculate_discount that calculates the discounted 
price of an item based on the original price and a discount rate 
(default to 10%). Return the discounted price.

def calculate_discount(price, discount = 0.1):
    discounted_price = price - (price * 0.1)
    return discounted_price

print(calculate_discount(200))


C. Create a function sum_all that takes any number of arguments using 
the asterisk operator in the parameter definition and returns the sum 
of all the arguments.

def summa(*numbers):
    return sum(numbers)

print(summa(1, 2, 3, 5, 7))


D. Write a function calculate_product that takes at least two arguments
and calculates their product. Use the asterisk operator in the parameter 
definition to handle multiple arguments.

def calculate_product(*args):
    product = 1
    for num in args:
        product *= num
    return product


E. Write a function sum_of_numbers that takes a variable number of integers
as parameters and returns their sum.

def summa(*numbers):
    return sum(numbers)

print(summa(4, 5, 6))

F. Create a function calculate_power that takes two parameters: a base number
and an exponent, and returns the result of raising the base to the given exponent.

def calculate_power(a , b):
    c = a ** b
    return c

print(calculate_power(3, 3))


G. Define a function named greet_user that takes a parameter username and prints 
a greeting message like: "Hello, [username]!".

def greet(username):
    print(f"Hello, {username}")

greet()

H. Write a function called calculate_area that takes the radius of a circle as a 
parameter and returns the area of the circle.

def calculate_area(r):
    S = 3.14 * r ** 2
    return S

print(calculate_area(1))


I. Create a function average that takes a list of numbers as a parameter and calculates 
the average of those numbers.

def average(lst):
    summ = sum(lst)
    length = len(lst)
    avg = summ/length
    return avg

lst = [1, 3, 3, 5]
print(average(lst))


J. Implement a function maximum_number that takes a variable number of integers as 
parameters and returns the largest number.

def maximum_number(*numbers):
    return max(numbers)

result = maximum_number(1, 3, 7, 99, 999)
print(result)



K. Define a function greet_with_salutation that takes a username and a salutation 
(with a default value of "Mr.") as parameters and prints a greeting using the provided salutation.

def greet_with_salutation(name, salutation = "Mr."):
    print(f"Hello {salutation} {name}")

greet_with_salutation()


L. Write a function calculate_cost that calculates the total cost of purchasing a
given quantity of items, considering a unit price and tax rate (default tax rate is 5%).

def calculate_cost(quantity, tax_rate = 0.05):
    unit_price = 100
    total_cost = (quantity * 100) * 0.05 + (quantity * 100)
    return total_cost

print(calculate_cost(2))



M. Create a function concatenate_strings that takes a variable number of strings as parameters 
and concatenates them into a single string, separated by spaces.

def concatenate_strings(*args):
    return ' '.join(args)



N. Write a function calculate_sum_and_product that takes at least two numbers as arguments 
and returns both their sum and product. Use the asterisk operator in the parameter definition 
to handle multiple arguments.

def calculate_sum_and_product(*args):
    result_sum = sum(args)
    result_product = 1
    for num in args:
        result_product *=num
    return result_sum, result_product

result = calculate_sum_and_product(3, 4, 5)
print(result)


O. Write a function find_max_min that takes a list of numbers as a parameter and returns both 
the maximum and minimum numbers from the list. Use if statements to handle edge cases.



def find_max_min(lst:list):
    return max(lst), min(lst)

print(find_max_min([2, 5, 9, 0, 89]))


OR


def find_max_min(numbers):
    min_num = 0
    max_num = 0

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return max_num, min_num
         
   
print(find_max_min([1, 3, 5, 89]))

P. Create a function calculate_grade that takes a student's numerical score as a parameter and
returns their corresponding letter grade based on the following scale:
90-100: 'A'
80-89: 'B'
70-79: 'C'
60-69: 'D'
Below 60: 'F'
Handle any invalid scores (less than 0 or greater than 100) by returning 'Invalid Score'.

def calculate(score):
    if score > 100 and score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print(calculate(55))


Q. Write a function solve_quadratic that takes the coefficients of a quadratic equation 
(a, b, c) as parameters and returns the real roots (if any) of the quadratic equation. 
Use the quadratic formula.

from math import sqrt
def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c
    x_1 = (- b - sqrt(D) / 2 * a)
    x_2 = (- b + sqrt(D) / 2 * a)
    return x_1, x_2

print(f" the root of quadratic equation are {solve_quadratic(1, 4, 3)}")


R. Implement a function is_palindrome that takes a string as a parameter and returns True
if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def is_palindrome(sentence:str):
    sentence = sentence.lower().strip()
    if sentence == sentence[::-1]:
        return True
    else:
        return False

print(is_palindrome("Bob"))


S. Create a function sort_numbers that takes three numbers as parameters and returns them in 
ascending order as a tuple.

def sort_numbers(a, b, c):
    result = tuple(sorted([a, b, c]))
    return result

print(sort_numbers(9, 2, 3))


T. Write a function calculate_tax that takes an income amount and a tax rate as parameters 
and calculates the tax amount. Return a tuple containing the tax amount and the net income 
(income after tax).

def calculate_tax(income, tax_rate):
    tax_amount = income * tax_rate / 100
    net_income = income - tax_amount
    return tax_amount, net_income

print(calculate_tax(1000, 20))

U. Create a function calculate_discounted_price that takes the original price and a discount 
percentage as parameters. Return a tuple containing the discounted price and the amount saved.

def calculate_discounted_price(original_price, discount):
    discounted_price = original_price - original_price * discount/100
    return discounted_price

print(calculate_discounted_price(100, 20))



Quiz.
1. What does the following function do?
    def greet_user(username):
        print("Hello, " + username + "!")

    a) Greets the user with a customized message.
   

2. Which of the following functions best describes the calculations of the area of a circle?
  
    d) calculate_area_circle(radius)

3. What is the purpose of a default parameter in a function?
  
    d) It is used to specify the default return value of the function.

4. In Python, how do you pass a variable number of arguments to a function?
   
    c) Using the asterisk (*) operator in the parameter definition
   

5. Which of the following functions best describes the calculations of the sum of a list of numbers?
 
    d) sum_all(*numbers)

6. What does the asterisk (*) operator do in the function definition?
   
    b) Allows the function to take a variable number of arguments.
    

7. Consider the following function:
    def greet_user(username="Guest"):
        print("Hello, " + username + "!")

    What is the default value for the username parameter in this function?
    a) "Guest"
  

8. In the following function, what happens if no value is provided for the message parameter?
    def greet_with_message(username, message="Hello"):
        print(message + ", " + username + "!")

    
    b) The function uses the default value "Hello" for the message.
    

9. Which of the following is a valid function definition using default parameters?
    a) def calculate_area(radius, pi=3.14159):
  
10. Consider the function below:
    def calculate_discount(price, discount_rate=0.1):
        return price * (1 - discount_rate)

    What is the default discount rate used if not provided?
    a) 10%


11. Given the function:
    def multiply(a, b=2):
        return a * b

    If we call multiply(5), what will be the result?
    a) 10
    

12. In the following function definition, what does the * represent?
    def display_names(*names):
        for name in names:
            print(name)

    
    b) It allows passing a variable number of names as arguments.


13. Given the function below:
    def greet_with_messages(*messages):
        for message in messages:
            print(message)

    If we call greet_with_messages("Hello", "Bonjour", "Hola"), how many messages will be printed?
    a) 3


14. Consider the function definition:
    def generate_pattern(symbol='*', count=5):
        return symbol * count

    If we call generate_pattern(count=3), what will be the result?
  
    d) '*****'

15. You have a list of numbers: [12, 5, 78, 43, 67, 89, 45, 23]. What will the function find_max_min return for this list?
  
    d) (89, 5)

16. If the score provided to the function calculate_grade is 75, what will be the output of the function?
    a) 'C'
  
   
17. For the quadratic equation with coefficients a=1, b=-5 and
c=6, what will the function solve_quadratic return?
   
    c) (2, 3)
   

18. If the input string to the function is_palindrome is "radar", 
what will the function return?
    a) True
 
      
19. For the input numbers 5, 2, 8, what will be the output of the function sort_numbers?
    a) (2, 5, 8)
    

20. If the income is $5000 and the tax rate is 20%, what will be the output of 
the function calculate_tax?
  
    b) (4000, 1000)
  

21. If the original price is $100 and the discount rate is 25%, what will be the 
output of the function calculate_discounted_price?
    a) (75.0, 25.0)
 """