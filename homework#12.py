"""
- Dictionaries -
A. Create a dictionary with you personal data (firstname, lastname, age, gender).

info = {
    "name": "Teymuraz",
    "surname": "Safarov",
    "age": 40,
    "gender": "male"
}
B. Create a dictionary with stock data of fruits (fruit name, amount in stock).

fruits = {
    "apple": 20,
    "orange": 15,
    "banana": 9,
    "kiwi": 7, 
}

C. Change any value of the dictionary from Task B.

fruits = {
    "apple": 20,
    "orange": 15,
    "banana": 9,
    "kiwi": 7, 
}
fruits["apple"] = 34

D. Create a dictionary about five students and their math grades.

students_grades = {
    "Mark": 5,
    "Bob": 5,
    "Kelly": 3,
    "Tim": 4
}

E. Add some points to any student from Task D's dictionary.

students_grades["Tim"] = 5

F. Create a dictionary about your favorite car model. Describe it as much 
as you can (brand, manufacturing contry, tires, color, year).

mercedes_char = {
    "year": 2020,
    "engine": 2.0,
    "color": "brown",
    "max_speed": 250,
    "model": "sedan",
    "country": "Germany"
}
G. Create a dictionary with all continents of the world with minimum 3 
countries (if possible) as its value.

continents = {
    "America": "USA",
    "Asia": "China",
    "Africa": "Senegal",
    "Europe": "Italy",
    "Australia": "Tasmania",
}

H. Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
and definition of those words as values. Print dictionary and its length.

dictionary = {
    "language": "Python",
    "cloth": "panths",
    "hobby": "football",
    "job": "developer",
    "country": "spain",
}
print(dictionary)
print(len(dictionary))

I. Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
and translation to russian language of those words as values.

translation = {
    "face": "лицо",
    "five": "пять",
    "opinion": "мнение",
    "look": "смотреть",
    "see": "видеть"
}

J. Fill in the blank:
As of Python version _3._6, dictionaries are ordered. In Python 3_._5 and earlier, 
dictionaries are unordered.

K. Describe dictionaries' main 3 characteristics

They are ordered, changeable and not allowed duplicates

L. Fill in the blank:

Only immutable objects or data types can be represented as keys in dictionaries.

M. Print all keys of dictionary from Task D.

print(students_grades.keys())


N. Print all values of dictionary from Task D.

print(students_grades.values())

O. Print all keys and values together of dictionary from Task D.

print(students_grades.items())

P. Suppose you have the following code snippet:

car = {
    "model": "Camaro",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "brand": "Chevrolet",
    "color": "red",
}
print(car)

What will be the output of the program and why?

{'model': 'Mustang', 'brand': 'Chevrolet', 'year': 1964, 'color': 'red'}

Because it's dictionary

Q. Change 'color' of 'car' dictionary to 'blue'.

car["color"] = "blue"
print(car)


R. Add any new key-value pair to 'car' dictionary.

car["country"] = "USA"
print(car)

S. Use the whole dictionary from Task A in a string formatted with:
    1. f-strings
    2. format
    3. %s

    1. info = f"Name is {name}.Surname is {surname}.Age is {age}.Gender is {gender}"
    2. info = "Name is {}. Surname is {}.Age is {}.Gender is {}".format(name,surname,age,gender)
    3. info = "Name is %s. Surname is %s. Age is %s. Gender is %s."%(name, surname, age, gender)

T. Create an empty dictionary. Print its length.

empty = {}
print(len(empty))

U. You have the following dictionary:
grades = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92,
    'Emily': 88
}

Ask user for a student name to add 7 points to the grade of that student.

name = input("enter students name:")
if name in grades:
    grades[name]+=7
print(grades)


V. You have the following dictionary:
word_definitions = {
    'apple': 'a round fruit with red or green skin and crisp flesh',
    'computer': 'an electronic device for processing and storing data',
    'book': 'a written or printed work consisting of pages',
    'ocean': 'a large body of saltwater that covers most of the Earth\'s surface',
    'mountain': 'a large natural elevation of the Earth\'s surface'
}

Ask user for an item name to to print the length of the definition of that item.

item = input("enter item name")
if item in word_definitions:
    print(len(word_definitions[item]))

- ChatGPT's homework (Dictionaries) -
A. Create a dictionary named student_scores with the following key-value pairs:

    "Alice": 85
    "Bob": 92
    "Eve": 78
    "Charlie": 95

Print out the dictionary student_scores.

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Eve": 78,
    "Charlie": 95
}
print(student_scores)


B. Add a new student "David" with a score of 88 to the dictionary.

student_scores["David"] = 88
print(student_scores)

C. Update Eve's score to 82.

student_scores["Eve] = 82

D. Remove Bob from the dictionary.

student_scores.pop("Bob")

E. Create a Python program that asks the user to enter a key, and then prints 
the corresponding value from the provided dictionary. If the key does not exist, 
it should print a message saying "Key not found.":
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key = input("Enter the key:")
if key in my_dict:
    print(my_dict[key])
else:
    print("Key not found")

F. Create a Python program that asks the user to enter a key and a value, and then 
adds this key-value pair to the provided dictionary:
1. Ask the user to enter a key and a value.
2. Add the entered key-value pair to the provided dictionary my_dict.
3. Print the updated dictionary.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key = input("Enter key:")
value = input("value:")
my_dict[key] = value
print(my_dict)

- I/O -
A. Write a program that gets the sides of a rectangle from the user, and
calculates its perimeter.

AB = float(input("Enter first side:"))
BC = float(input("Enter second side:"))
P = (AB + BC) * 2
print(P)

B. Write a program that gets the sides of a rectangle from the user, and
calculates its area.

AB = float(input("Enter first side:"))
BC = float(input("Enter second side:"))
S = AB * BC
print(S)

C. Write a program that gets the sides of a square from the user, and
calculates its perimeter.

AB = float(input("Enter the side:"))
P = AB * 4
print(P)

D. Write a program that gets the sides of a square from the user, and
calculates its area.

AB = float(input("Enter the side:"))
S = AB ** 2
print(S)


E. Write a program that gets the radius of a circle from the user, and
calculates its area.

radius = float(input("Enter the radius:"))
S = 3.14 * radius ** 2
print(S)

F. Write a program that gets the diameter of a circle from the user, and
calculates its length.

diameter = float(input("Enter the diameter:"))
L = 3.14 * diameter
print(L)



- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz.
1. What is a dictionary in Python?
    
    b) A collection of key-value pairs
    c) A collection of unique elements
    d) A collection of elements in a specific order

2. How do you create an empty dictionary in Python?
    a) my_dict = {}
    b) my_dict = dict()
 

3. How do you access a value in a dictionary using its key?
    
    b) my_dict[key]
  
    
4. Can a dictionary have duplicate keys?
   
    b) No
    
5. How do you add a new key-value pair to an existing dictionary?
    
    b) my_dict[key] = value
  
    
6. How do you remove a key-value pair from a dictionary?
   
    d) my_dict.pop(key)
    
7. Which method returns a list of all the keys in a dictionary?
    a) my_dict.keys()
 

8. How do you check if a key is in a dictionary?
    a) key in my_dict
   

9. What happens if you try to access a key in a dictionary that doesn't exist?
    a) It raises a KeyError


10. Which dictionary method is used to retrieve the value associated with a key, 
and if the key does not exist, return a default value instead of raising an error?
    a) get(key, default)
   

11. Which dictionary method is used to remove all key-value pairs from the dictionary?
    a) clear()
  

12. Which dictionary method returns a new dictionary with keys from the given sequence and 
values set to a specified value?
    a) fromkeys(seq, value)
  

13. Which dictionary method returns a list of tuples, each tuple containing a key-value pair 
from the dictionary?
    a) items()
 
14. Which dictionary method returns a list of all the values in the dictionary?
    a) values()


15. Which dictionary method returns and removes an element with a specified key?
    a) pop(key)

    
16. Which dictionary method returns a shallow copy of the dictionary?
    a) copy()
  
17. Which dictionary method is used to update the dictionary with key-value pairs 
from another dictionary or from an iterable of key-value pairs?
    a) update(iterable)


18. Which dictionary method returns the value for a specified key and removes the 
key-value pair from the dictionary?
    a) popitem()
    
    
19. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict.get('b'))

   
    b) 2
    
        
20. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict['d'] = 4
    print(my_dict)
    

    b) {'a': 1, 'b': 2, 'c': 3, 'd': 4}
 
    
21. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.pop('b')
    print(my_dict)

    a) {'a': 1, 'c': 3}
 

22. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(list(my_dict.items()))

    a) [('a', 1), ('b', 2), ('c', 3)]
   
    
23. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.update({'b': 5, 'd': 4})
    print(my_dict)

    
    b) {'a': 1, 'b': 5, 'c': 3, 'd': 4}
  

24. What is the main difference between the pop() and popitem() methods in Python dictionaries?

    a) pop() allows you to remove a specific key-value pair by providing the key, while popitem() 
    removes and returns an arbitrary key-value pair.
   
   
"""