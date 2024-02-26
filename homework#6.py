"""
Note. Use appropriate variable names while completing the tasks.

- Integers -
A. Create a variable called 'speed'. Assign any integer value between 60 and 80 to it.

speed = 70

B. Create a variable called 'limit'. Assign any integer value between 90 and 110 to it.

limit = 100

C. Create a variable called 'difference'. Make it equal the difference between the
'limit' and the 'speed' variable. Print the 'difference' variable.

difference = limit - speed
print(difference)
D. Create a variable called 'amount'. Assign any integer value between 5 and 20 to it.

amount = 15

E. Create a varaible called 'double_amount'. Make it equal the double value of the 'amount'
variable.

double_amount = amount * 2

F. Create a varaible called 'triple_amount'. Make it equal the triple value of the 'amount'
variable. Print these variables (amount, double_amount, triple_amount) separately.

triple_amount = amount * 3

print(amount)
print(double_amount)
print(triple_amount)

G. Create a variable called 'distance'. Assign any integer value between 500 and 2000 to it.

distance = 1000
H. Create a variable called 'passed_distance'. Assign any integer value between 100 and 500 to it.

passed_distance = 300

I. Print the difference between the 'distance' variable and the 'passed_distance' variable.

print(passed_distance - distance)

J. Create a variable called 'number_one'. Give it any integer value.

number_one = 9

K. Create a variable called 'number_two'. Give it any integer value.

number_two = 27


L. Create a variable called 'number_three'. Make it equal to the sum of 'number_one' and 'number_two'.
Print the value of 'number_three' variable.

number_three = number_one + number_two
print(number_three)
M. Create a variable called 'a'. Make it equal 15.
a = 15
N. Create a variable called 'b'. Make it equal 35.
b = 35
O. Create a variable called 'c'. Make it equal 20.
c = 20
P. Create a variable called 'result'. Make it equal the sum of 'a' and 'b' minus 'c'. Print its value.
result = a + b - c
print(result)
Q. Create a variable called 'my_number'. Make it equal 4.
my_number = 4
R. Print 'my_number's raised to the third power value.
print(my_number**3)

- Floats -
A. Create a variable called 'temperature'. Make it equal any float number.
temperature = 25.5
B. Create a variable called 'weight'. Make it equal any float number.
weight = 70.5
C. Create a variable called 'length'. Make it equal any float number.
length = 175.6
D. Create a variable on your own (name it appropriately). Make it equal any float number.
body_lenght = 178.8
E. Print all those variables from Task A to D.
F. Create a variable called 'x'. Make it equal any float number between 1 and 2 with 2 decimal points.
x = 1.56
G. Create a variable called 'double_x'. Make it equal double-value of 'x'
double_x = x * 2
H. Print all those variables from Task F to G.
I. Make your best and create a hard task by your own using floats.

body_length = 180.5
body_weight = 80
print(f"Hello. You are {body_length} centimeter tall, and {body_weight} weight.")

- Built-in functions -
A. Create a variable called 'long_sentence'. 

Make it equal a long sentence. Print 'long_sentence's length.

long_sentence = "long sentence"
print(len(long_sentence))

B. Create a variable called 'accurate_number'.
Make it equal any float number between 10 and 11 with 5 decimal points
Print this variable.

accurate_number = 10.12345
print(accurate_number)

C. Create a variable called 'rounded_accurate_number'.
Make it equal the 'accurate_number's value rounded to 2 decimal points.
Print this variable.

rounded_accurate_number = round(accurate_number,2)
print(rounded_accurate_number)

D. Override 'rounded_accurate_number' variable.
Make it equal the 'accurate_number's value rounded to 3 decimal points.
Print this variable.

rounded_accurate_number = round(accurate_number,3)
print(rounded_accurate_number)

E. Using 'round' method round 175233, so it gives us 175000.

print(round(175233,-3))

- Math module -
A. Find the 'math' module's method by its definition:
1. The math.sqrt()  method returns the square root of a number.
2. The pow() method returns the value of x raised to power y.
3. The math. ceil() method rounds a number UP to the nearest integer, if necessary, 
and returns the result.
4. The math. floor() method rounds a number DOWN to the nearest integer, if necessary, 
and returns the result.
B. Round π (Pi) to two decimal places.
print(round(Pi,2))

C. The area of a square is 700 square units. Find the side of that square.
square = 700
side = math.sqrt(square)
print(side)
D. One side of a rectangle is 5 units longer than other side. Find the area of
rectangle, if the perimeter is 100 units.

''' first_side = x
    second_side = x + 5
    x + x + x + 5 +x +5 = 100
    4x = 90
    x = 22.5  first_side'''
    AB = 22.5
    AC = 27.5
    S = AB * AC
    print(S)


E. Round 5.7 down to the nearest integer.

math.floor(5.7)
F. Round 5.7 up to the nearest integer.

math.ceil(5.7)


- Expressions - 
Simplify these expressions:
A. (5 * 5 + 5 // (5 + 5 % 5) // 5) + 5**5 + 5 - 5**0

(25 + 0) + 25 + 5 - 1 = 54

B. (20 + 30 * (15 - 7) // (3 + 4 % 2) + 10**2 // 5) + 2**6 + 50 - 3**1

20 + 30 * 2  + 20 + 2**6 +50 - 3 = 1011

C. (70 - 25 + 3 * (8 + 4) // (6 + 9 % 3) + 15**2 // 7) + 4**3 + 90 - 2**4

70 - 25 + 3*2 + 32 + 4**3 + 90 - 2*4 = 224

- Chat GPT's Homework - 
Task 1. Mixed Operations and Variable Naming
Solve the following mixed arithmetic expressions, using appropriate variable names:
a) Calculate the perimeter of a square with side length 6 units.
AB = 6
S = AB**2
print(S)

b) You have $150. If you spend $47.25 and then receive $30.50, how much money do you have left?

'''' 150 - 47.25 + 30.50 = 133.25
    150 - 133.25 = 16.75 '''


c) A train is moving at a speed of 80 km/h. How far will it travel in 1.5 hours?

speed = 80
time = 1.5
s = speed * time
print(s) # 120 km

Task 2. Float Operations
Perform the following floating-point operations and round the answers to two decimal places:
a. 4.25 + 2.68 = 6.93   round(6.93,2)
b. 9.75 - 3.85 = 5.90   round(5.90,2)
c. 3.5 x 1.2   = 4.20   round(4.20,2)
d. 7.8 / 2.5   = 3.12   round(3.12,2S)

Task 3. Accessing the Value of π (Pi)

A. Use the math.pi attribute to access the value of π (Pi) and store it in a variable.
Pi = 3.14
B. Calculate and print the circumference of a circle with a radius of 7 units using 
the π value from the math.pi attribute.

radius = 7
circle_length = 2 *Pi * radius
print(circle_length)


Task 4. Using 'sqrt' Method
A. Calculate and print the square root of 16 using the math.sqrt() method.
print(math.sqrt(16))
B. Calculate and print the square root of 25 using the math.sqrt() method.
print(math.sqrt(25))
C. Calculate and print the square root of 10 using the math.sqrt() method.
print(math.sqrt(10))

Task 5. Using 'pow' Method
A. Calculate and print the result of raising 2 to the power of 5 using the math.pow() method.
print(math.pow(2,5))

B. Calculate and print the result of raising 3 to the power of 4 using the math.pow() method.
print(math.pow(3,4))

Task 6. Use the math.ceil() method to round the following numbers up to the nearest integer:
a. 6.1    math.ceil(6.1) # 7
b. 10.9   math.ceil(10.9) # 11
c. -2.3   math.ceil(-2.3) # -3

Task 7. Use the math.floor() method to round the following numbers down to the nearest integer:
a. 4.7   math.floor(4.7)  # 4
b. 9.2   math.floor(9.2)  # 9
c. -3.8  math.floor(-3.8) # -3 

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.

# There were various one-line comments, as you can see in code above

B. Multi-line comment anywhere in your code, if it's appropriate.

''' There were no reasons
    to create multi-line comments,
    except one in this task,
    according homework '''

Quiz:
1. Which of the following is a comparison operator in Python?
    c) ==

2. What is the result of 15.5 - 7.2 rounded to two decimal places?
    a) 8.3


3. What is the result of 1.5 - 1.0 rounded to two decimal places?
    a) .5
    

4. If 'a = 12' and 'b = 7', which expressions are True?
    
    b) a > b

5. What is the value of 20/4?
    a) 5
    

6. Which of the following are integers?
    
    b) -15
    e) int("1")

7. What is the absolute value of -25?
    a) 25
   

8. If 'x = 5' and 'y = 8', what is the value of x^y (x raised to power of y)?
   
    d) 390625

9. What does the math module in Python provide?
   
    d) A set of mathematical functions and constants.

10. Given the equation 3 x 8 - 5, what is the correct result?
    a) 19
    

11. What is the result of 17 + 23?
    
    b) 40
   

12. What is the result of "17" + "23"?
    
    d) "1723"
    
"""