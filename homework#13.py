"""
Instructions: Write Python code for each of the following tasks. 
Make sure to use if statements appropriately to achieve the desired outcomes. 
If appropriate, comment your code to explain each step.

- If Statements -
A. Create any variable with Boolean value. Print 'My variable evaluates to True'
if this variable is 'True', otherwise print 'My variable evaluates to False'.

name = True
if name == True:
    print(f"My variable evaluates to {name}")
else:
    print("My variable evaluates to False")


B. Create a variable named 'temperature'. Make it equal to any degree. Check:
1. If temperature is under 10 degrees, print 'It\'s cold outside, take a scarf.'.
2. If temperature is in interval from 10 to 24 degrees (both included), print 
'It\'s a nice weather. Let\'s go for a walk.'.
3. If temperature is above 24 degrees, print 'It\'s quite hot, I need an AC.'.

temperature = 15
if temperature < 10:
    print("It\'s cold outside, take a scarf")
elif  10 <= temperature <= 24:
    print("It\'s a nice weather. Let\'s go for a walk.")
else:
    print("It\'s quite hot, I need an AC.")


C. Create a variable named 'age'. Make it equal your age. Check:
1. If it's under 18, print 'I am not eligible for voting :('
2.If you are 18 or older, print 'I am eligible for voting!'

age = 40
if age < 18:
    print("I am not eligible for voting :(")
else:
    print("I am eligible for voting!")


D. Create variables 'a' and 'b'. Make them equal 15 and 20 correspondingly.
Check if their sum gives less than 40, print their sum and add 'It\'s less than 40.'.
Otherwise, print their sum and add 'It makes 40 or more than 40.'.

a = 15
b = 20
summ = a + b
if summ < 40:
    print(f"{summ} It\'s less than 40.")
else:
    print(f"{summ} It makes 40 or more than 40.")


E. Create a list with 4 students (make it contain their names). Check if the 
length of that list is less than 5, add new student to that list.

lst = ["Mark", "Bob", "Tim", "John"]
if len(lst) < 5:
    lst.append("Jenny")
print(lst)

F. Create four variables (a, b, c, d) with numeric (int & float) values.
Write the logical expression to check if 'a' is greater than 'b' and 'c' is greater
than 'd'.

a = 10
b = 3.0
c = 21
d = 14.5
if a > b:
    print("a is greater than b")
if c > d:
    print("c is greater than d")


G. Write a program to check whether a number accepted from user is divisible by 2
and 3 both.

number = int(input("Enter number:"))
if number % 2 == 0 and number % 3 == 0:
    print("It's divisinble by 2 and 3 both")
else:
    print("At least one condition is not true")


H. Write a program that finds the largest number out of three numbers accepted from user.

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if a > b and a > c:
    print("a is maximal")
elif a == b and a > c:
    print("a and b are equal and bigger than c")
elif a > b and a == c:
    print("a and c are equal and bigger than b")
elif b > a and b > c:
    print("b is maximal")
elif b == a and b > c:
    print("b and a are equal and bigger than c")
elif b > a and b == c:
    print("b and c are equal and bigger than a")
elif c > a and c > b:
    print("c is maximal")
elif c == a and c > b:
    print("c and a are equal and bigger than b")
elif c > a and c == b:
    print("c and b are equal and bigger than a")

I. Write a program that gets any input from user. It should print 'Lower job!' if all
characters in user's input are lowercase, otherwise print 'Upper job!'.

sentence = input("enter any sentence:")
if sentence.islower():
    print("Lower job")
else:
    print("Upper job")


J. Write a program to check whether a number entered by user is three digit number or not.

number = int(input("enter number:"))
if len(str(number)) == 3:
    print("this is three digit number")
else:
    print("this is not three digit number")


    OR

number = int(input("enter number:"))
if number // 100 >=1 and number // 100 <=9:
    print("this is three digit number")
else:
    print("NOT")


K. Accept the temperature in degree Celcius of water and check whether it's boiling or
not (boiling point of water is 100 degree Celcius).

temperature = int(input("Enter the water temperature in Celsius:"))
if temperature == 100:
    print("It's boiling temperature")
else:
    print("It's not boiling temperature")

L. Accept the IQ of 3 people and display the highest one.

first_iq = int(input("enter IQ:"))
second_iq = int(input("enter IQ:"))
third_iq = int(input("enter IQ:"))
if first_iq > second_iq and first_iq > third_iq:
    print(f"the highest is {first_iq}")
elif second_iq > first_iq and second_iq > third_iq:
    print(f"the largest is {second_iq}")
elif third_iq > first_iq and third_iq > second_iq:
    print(f"the largest is {third_iq}")


M. Write a program to check whether a character accepted from user is vowel or not.

vowel = ["a", "o", "u", "i", "e"]
char = input("enter any char:")
if char in vowel:
    print("This char is vowel")
else:
    print("This char is not vowel")

N. Accept the following from the user and calculate the percentage of class attendance:
1. Total number of class days
2. Total number of days for absence
O. Accept the percentage from the user and display the grade according to the following
criterias:
1. Below 25 - D
2. 25 to 45 - C
3. 45 to 50 - B
4. 50 to 60 - B+
5. 60 to 80 - A
6. Above 80 - A+


total_days = int(input("Enter total class days:"))
absence_days = int(input("Enter absence days:"))
result = absence_days / total_days * 100
if result < 25:
    print("your grade is D")
elif result >= 25 and result < 45:
    print("your grade is C")
elif result >= 45 and result < 50:
    print("your grade is B")
elif result >= 50 and result < 60:
    print("your grade is B +")
elif result >= 60 and result <= 80:
    print("your grade is A")
elif result > 80:
    print("your grade is A +")

- Dictionary Methods -
A. Create a nested dictionary. Get any inner value using multiple key-indexing.

nested_dict = {
    'person1': {
        'name': 'Tim',
        'age': 40},
        'person2': {
        'name': 'Bob',
        'age': 30,}
}

print(nested_dict["person1"]["name"])

B. Create a dictionary with your personal data (name, surname, age, family status,
gender). Ask user for any key in your dictionary. Print the value of the given
key from the dictionary. Try to ask all keys.

info = {"name": "Tim",
        "surname": "Safarov",
        "age": 40,
        "job": "developer"

}
print(info["surname"])

print(info.keys())

C. Create a dictionary with stock data of clothes (cloth name + amount). Let 
the user choose any of keys and add some count to it.

cloth = {
    "hat": 3,
    "pants": 9,
    "shirts": 25,
    "shoes": 8,
    "socks": 10
}
cloth["socks"]+=15
print(cloth)

D. Copy any dictionary from previous tasks. Print it.

cloth = {
    "hat": 3,
    "pants": 9,
    "shirts": 25,
    "shoes": 8,
    "socks": 10
}
dubl = cloth.copy()
print(dubl)

E. Clear the dictionary from Task D. Print the length of this dictionary.

TypeError: object of type 'NoneType' has no len()

F. Create an empty dictionary. Let the user add data to it (key & value). Choose
any topic (books, cars, info, items, grades...) and let the user fill it with
minimum 4 key-value pairs.

my_dict = {}
countries = input("Enter 4 countries and separate them by space:").split()
capitals = input("Enter the capitals of this countries and separate them by space:").split()
my_dict = dict(zip(countries, capitals))
print(my_dict)

G. You have the following dictionary:
car = {
    "brand": "Chevrolet",
    "model": "Camaro",
    "year": 2017
}

Create a 'not_found_message' variable. Make it equal appropriate "not found" message.
Try to get 'year's and 'color's values from the 'car'. Set the default value to 
our "not found" message.

not_found_message = "not found"
print(car.get("color", not_found_message))

H. Print the first 6 keys from the following dictionary (hint: you should use 
'list()' method to convert dict_keys to list and indexing to get the appropriate
portion of data):
countries_capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "India": "New Delhi",
    "South Africa": "Pretoria",
}

lst = list(countries_capitals)
print(lst[0:6])

I. You have the following dictionary:
programming_languages = {
    "Python": {
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "High"
    },
    "JavaScript": {
        "designed_by": "Brendan Eich",
        "first_appeared": 1995,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "Very High"
    },
    "Java": {
        "designed_by": "James Gosling",
        "first_appeared": 1995,
        "paradigm": "Object-oriented",
        "typing": "Static",
        "popularity": "High"
    },
    "C++": {
        "designed_by": "Bjarne Stroustrup",
        "first_appeared": 1985,
        "paradigm": "Multi-paradigm",
        "typing": "Static",
        "popularity": "Moderate"
    }
}

Using in f-strings print the year Python was appeared value.

print(f"The year Python first appeared is {programming_languages["Python"]["first_appeared"]}")


J. You have the following code snippet:
tasks = {
    "Alice": ["Buy groceries", "Finish report", "Call the doctor"],
    "Bob": ["Walk the dog", "Pay bills", "Read a chapter"]
}

selected_person = "Alice"
new_task = "Go to the gym"

Add the new task to the selected person's tasks. Print the tasks & length of tasks 
before and after edition.

print(len(tasks))
selected_person = "Alice"
new_task = "Go to the gym"
tasks[selected_person].append(new_task)
print(len(tasks))

K. There is a dictionary method that helps to create a dictionary with a collection
of keys and apply a default value to that key. Using that method create a dictionary
with all values equal to the '[0, 4, 8, 12, 16, 20]' list and keys should only be
the numbers from 0 to 4, so your dictionary should look like:
digits = [1, 2, 3, 4, 5]

my_dict = {
    0: [0, 4, 8, 12, 16, 20],
    1: [0, 4, 8, 12, 16, 20],
    2: [0, 4, 8, 12, 16, 20],
    3: [0, 4, 8, 12, 16, 20],
    4: [0, 4, 8, 12, 16, 20],
}

You should use list comprehension in this task.

Then you should print some portion from the list values of a dictionary. The
portion size depends on a key you are using to index the list.

keys = [0, 1, 2, 3, 4]
lst = [0, 4, 8, 12, 16, 20]
my_dict = dict.fromkeys(keys, lst)
print(my_dict)
print(my_dict[1][1:3])


L. Print all items, values, keys from 'programming_languages' dictionary.

print(programming_languages.items())
print(programming_languages.keys())
print(programming_languages.values())





M. Remove 'Java' from 'programming_languages' dictionary & get its value. Print it.

print(programming_languages["Java"])
programming_languages.pop("Java")
print(programming_languages)


N. Remove the last item from the following dictionary and print it:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("year")
print(car)

O. Expand 'programming_languages' dictionary with the following data:
language_to_add = {
    "PHP": {
        "designed_by": "Rasmus Lerdorf",
        "first_appeared": 1995,
        "paradigm": "Server-side scripting",
        "typing": "Dynamic",
        "popularity": "Moderate"
    }
}

programming_languages.update(language_to_add)
print(programming_languages)


P. Use 'setdefault' method on any dictionary.

countries_capitals.setdefault("Germany", "Berlin")

Q. Which Data Types can be represented as values of any dictionary?

All data types

R. In the following example:
data = {
    "Python3.x": {
        "Wep Development", "Machine Learning", "Penetration Testing", "Game Development"
    }
}

It's giving an error if you try to get 'Python2.x' in this way:
data["Python2.x"]
Edit this code so it doesn't return an error.

data["Python2.x"] = {"Data Analitics", "Machine Learning", "Web Development"}
print(data["Python2.x"])

- Chat GPT's Homework -
Task 1.
Create an empty dictionary called student_info.
Add the following key-value pairs to the dictionary:
"name": "John Doe"
"age": 20
"major": "Computer Science"

student_info = {}
new_info = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science"
    }
student_info.update(new_info)
print(student_info)

Task 2.
Print the value associated with the key "name" from the student_info dictionary.
Change the value of the "age" key to 21.
Add a new key-value pair: "gender": "Male".

print(student_info["name"])
student_info["age"]+=1
student_info["gender"] = "Male"
print(student_info)

Task 3.
Create a new dictionary called grades with the following data:
"math": 85
"english": 92
"history": 78
Use the update method to add the key-value pairs from the grades dictionary into the student_info dictionary.

grades = {
"math": 85,
"english": 92,
"history": 78
}
student_info.update(grades)

Task 4.
Remove the "history" key from the grades dictionary using the pop method, and print the value that was removed.
Remove the "major" key from the student_info dictionary using the del statement.

grades.pop("history")
print(grades)
print(grades.get("history"))
del grades["math"]
print(grades)

Task 5: Basic If-Else Statements
Write a Python program that does the following:
Takes an integer input from the user.
Checks if the input is greater than 10.
If it is, prints "The number is greater than 10."
If it's not, prints "The number is not greater than 10."

number = int(input("Enter the number:"))
if number > 10:
    print("The number is greater than 10")
else:
    print("The number is not greater than 10")

Task 6: Multiple Conditions
Write a Python program that:
Takes two integer inputs from the user.
Checks if both numbers are even (divisible by 2).
If both are even, prints "Both numbers are even."
If at least one is not even, prints "At least one number is not even."

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("Both numbers are even")
else:
    print("At least 1 number is not even")

Task 7: Grade Calculator
Write a Python program that:
Takes a numerical score as input from the user (0 to 100).
Uses if-elif-else statements to determine the corresponding letter grade based on the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Prints the calculated letter grade.


score = int(input("Enter any number from 0 till 100:"))
if 0 < score < 59:
    print("Letter grade is F")
elif 60 < score < 69:
    print("Leter grade is D")
elif 70 < score < 79:
    print("Letter grade is C")
elif 80 < score < 89:
    print("Letter grade is B")
elif 90 < score < 100:
    print("Letter grade is A")

Task 8: Leap Year Checker
Write a Python program that:
Takes a year as input from the user.
Checks if the year is a leap year or not.
A leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400.
Prints "Leap year" or "Not a leap year" accordingly.

year = int(input("Enter the year:"))
if year % 400 == 0 and year % 100 == 0:
    print("Leap year!")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")

Task 9: Temperature Converter
Write a Python program that:
Takes a temperature in Celsius as input from the user.
Converts it to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
Prints the temperature in Fahrenheit.

Celsius = float(input("Enter the temperature in Celsius:"))
Fahrenheit = (Celsius * 9/5) + 32
print(f"the temperature in Fahrenheis is {Fahrenheit}")

Task 10: Number Comparison
Write a Python program that:
Takes three integer inputs from the user.
Determines and prints the largest of the three numbers using if-else statements.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b and a > c:
    print("a is maximal")
elif a == b and a > c:
    print("a and b are equal and bigger than c")
elif a > b and a == c:
    print("a and c are equal and bigger than b")
elif b > a and b > c:
    print("b is maximal")
elif b == a and b > c:
    print("b and a are equal and bigger than c")
elif b > a and b == c:
    print("b and c are equal and bigger than a")
elif c > a and c > b:
    print("c is maximal")
elif c == a and c > b:
    print("c and a are equal and bigger than b")
elif c > a and c == b:
    print("c and b are equal and bigger than a")

Task 11: Positive or Negative
Write a Python program that:
Takes an integer as input from the user.
Checks if the number is positive, negative, or zero.
Prints "Positive," "Negative," or "Zero" accordingly.

number = float(input("enter any number:"))
if number > 0:
    print("this number is positive")
elif number < 0:
    print("this number is negative")
else:
    print("Zero")

Task 12: Eligibility Checker
Write a Python program that:
Takes the age and citizenship status (True for U.S. citizen, False for non-U.S. citizen) as input from the user.
Checks if the person is eligible to vote in the U.S. based on the following conditions:
Must be at least 18 years old.
Must be a U.S. citizen.
Prints "You are eligible to vote" or "You are not eligible to vote" accordingly.

age = int(input("enter the age:"))
citizenship = input("enter your citizenship:")
if age >= 18 and citizenship == "U.S":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

Task 13: Password Strength Checker
Write a Python program that:
Takes a password as input from the user.
Checks the strength of the password based on the following criteria:
At least 8 characters long.
Contains both uppercase and lowercase letters.
Contains at least one digit (0-9).
Prints "Strong password" or "Weak password" accordingly.

password = input("Enter your password: ")
if len(password) < 8:
        print("Weak password")
elif not any(x.isupper() for x in password):
        print("Weak password")
elif not any(x.islower() for x in password):
        print("Weak password")
elif not any(x.isdigit() for x in password):
        print("Weak password")
else:
        print("Strong password")


OR


password = input("Enter your password: ")
if len(password) > 8 and any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) :
        print("Strong Password")
else:
        print("Weak password")

Task 14: Rock-Paper-Scissors Game
Write a Python program that:
Implements a simple text-based rock-paper-scissors game.
Takes the player's choice as input (rock, paper, or scissors).
Generates a random choice for the computer.
Determines the winner based on the game rules.
Prints the result of the game (win, lose, or tie) and the computer's choice.


import random
user_choice = input("Enter your choice rock, paper, or scissors:")
print(user_choice)
computer_choice = random.choice(["rock", "paper", "scissors"])
print(computer_choice)
if user_choice == "rock" and computer_choice == "rock":
    print("Play once again, there is no winner")
elif user_choice == "rock" and computer_choice == "paper":
    print("You are lose")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win")
elif user_choice == "scissors" and computer_choice == "scissors":
    print("Play once again, there is no winner")
elif user_choice == "paper" and computer_choice == "paper":
    print("Play once again, there is no winner")    


    OR


    import random
options = ["rock", "scissors", "paper"]
user_win = ["rockscissors", "scissorspaper", "paperrock"]
user_choice = input("Enter scissors, paper or rock:")
print(f"Your choice is {user_choice}")
comp_choice = random.choice(options)
print(f"Computer choice is {comp_choice}")
if user_choice == comp_choice:
    print("Tie")
else:
    print("You win") if (user_choice + comp_choice) in user_win else print("Comp win")

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.



Quiz. (If-Statements)
1. What is the keyword used to define an 'if' statement in Python?
    a) if
   

2. How do you write an if statement in Python?
    a) if condition:
 

3. In Python, what is the symbol for 'not equal to' in an if statement?
    
    b) !=
    

4. In Python, what is the purpose of the 'elif' statement?
 
    c) It is executed if the 'if' condition is False.
  

5. What will be the output of the following Python code?
    if 10 > 5:
        print("10 is greater than 5")
    else:
        print("This will not be printed")

    a) 10 is greater than 5
 

6. What is the output of the following Python code?
    x = 15
    if x < 10:
        print("x is less than 10")
    elif x < 20:
        print("x is less than 20 but greater than or equal to 10")
    else:
        print("x is 20 or greater")

   
    b) x is less than 20 but greater than or equal to 10

7. What is the primary purpose of an 'if' statement in Python?
    a) To execute a specific block of code based on a condition.


8. When is an 'else' statement used in conjunction with an 'if' statement?
    
    b) To execute the code block if none of the 'if' or 'elif' conditions are True.

9. Consider the following Python code. What will be printed if the variable 'num' is greater than or equal to 20?
    num = 25
    limit = 20

    if num >= limit:
        print("The number is greater than or equal to the limit")
    else:
        print("The number is less than the limit")

    a) The number is greater than or equal to the limit
   

10. Given the Python code snippet:
    num = 15

    if num > 10:
        print("num is greater than 10")

    What will be the output if this code is executed?

    a) num is greater than 10


11. Given the Python code snippet:
    x = 15

    if x > 10 and x < 20:
        print("x is greater than 10 and less than 20")
    else:
        print("x is either less than or equal to 10 or greater than or equal to 20")

    What will be the output if this code is executed?
    a) x is greater than 10 and less than 20
   

12. Given the Python code snippet:
    y = 5

    if y < 0 or y > 10:
        print("y is less than 0 or greater than 10")
    else:
        print("y is between 0 and 10 (inclusive)")

    What will be the output if this code is executed?

    b) y is between 0 and 10 (inclusive)
  

13. Given the Python code snippet:
    x = 8

    if x < 10:
        print("Code block 1: x is less than 10")
    elif x < 15:
        print("Code block 2: x is less than 15")
    elif x < 20:
        print("Code block 3: x is less than 20")
    else:
        print("Code block 4: x is 20 or greater")

    What will be the output if this code is executed when x is 8?
    a) Code block 1: x is less than 10
  

14. Given the Python code snippet:
    y = 25

    if y < 10:
        print("Code block 1: y is less than 10")
    elif y < 15:
        print("Code block 2: y is less than 15")
    elif y < 20:
        print("Code block 3: y is less than 20")
    else:
        print("Code block 4: y is 20 or greater")

    What will be the output if this code is executed when y is 25?
   
    d) Code block 4: y is 20 or greater
        
Quiz. (Dictionaries)
1. Which of the following are true of Python dictionaries:
    a) Dictionaries are mutable
    d) Dictionaries can be nested to any depth
    e) Dictionaries are accessed by key
    

2. Consider this dictionary:
    d = {'foo': 100, 'bar': 200, 'baz': 300}
    What is the result of this statement:
    d['bar':'baz']

    a) (200, 300)
    b) [200, 300]
    c) 200 300
    d) It raises an exception

3. Suppose x is defined as follows:
    x = [
        'a',
        'b',
        {
            'foo': 1,
            'bar':
            {
                'x': 10,
                'y': 20,
                'z': 30
            },
            'baz': 3
        },
        'c',
        'd'
    ]

What is the expression involving x that accesses the value 30?

x[2]['bar']['z']

4. Select the correct ways to get the value of marks key.
    student = {
    "name": "Emma",
    "class": 9,
    "marks": 75
    }

    
    b) m = student.get('marks')
  

5. Dictionary keys must be immutable:
    a) True
    

6. Select the all correct way to remove the key marks from a dictionary:
    student = { 
        "name": "Emma",
        "class": 9,
        "marks": 75
    }

    a) student.pop("marks")
 

7. What is the output of the following dictionary operation:
    dict1 = {"name": "Mike", "salary": 8000}
    temp = dict1.get("age")
    print(temp)

   
    b) None

8. Items are accessed by their position in a dictionary and all the keys in a 
dictionary must be of the same type:
   
    b) False

9. Select all correct ways to copy a dictionary in Python:
    a) dict2 = dict1.copy()
    b) dict2 = dict(dict1)
    

10. Please select all correct ways to empty the following dictionary:
    student = { 
        "name": "Emma", 
        "class": 9, 
        "marks": 75 
    }
  
    c) student.clear()

11. What is the output of the following:
    sample_dict = dict([
        ('first', 1),
        ('second', 2),
        ('third', 3)
    ])
    print(sampleDict)

    
    b) Options: SyntaxError: invalid syntax
    

12. Select the correct way to access the value of a history subject:
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    a) sample_dict['class']['student']['marks']['history']
   

13. Select the correct way to print Emma's age:
    student = {
        1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
        2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}
    }

    
    b) student[1]["age"]
  

14. What is the output of the following dictionary operation:
    dict1 = {"name": "Mike", "salary": 8000}
    temp = dict1.pop("age")
    print(temp)

    
    b) None

15. What is the output of the following code:
    dict1 = {"key1": 1, "key2": 2}
    dict2 = {"key2": 2, "key1": 1}
    print(dict1 == dict2)

    a) True
   

16. Select correct ways to create an empty dictionary:
    a) sample_dict = { }
    b) sample_dict = dict()

"""