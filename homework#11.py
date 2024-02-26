"""
- Tuples -
A. Create a tuple containing minimum seven different colors.

colors = ("red", "blue", "green", "white", "brown", "black", "yellow")

B. Create a tuple containing minimum five different countries.

countries = ("Azerbaijan", "Georgia", "Germany", "Italy", "Spain")

C. Create a tuple containing three string values and two integer values.

values = ("Hello", "Bye", "Good", 9, 18)

D. Create a tuple containing all continents of the world.

continents = ("Eurasia", "Africa", "North America", "South America", "Australia", "Antarktida")

E. Create a tuple containing minimum four car brands.

car_brands = ("Opel", "Mercedes", "Volkswagen", "Volvo")

F. Create a tuple containing four different data types of Python.

data_types = ("Wolrd", 3, True, [1,3])

G. Create a tuple containing only negative even numbers from -2 to -12.

negative_numbers = (-2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12)

H. Create a tuple containing only positive even numbers from 0 to 12.

positive_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

I. Combine tuples from Task G and H.

combined_numbers = (5, 9, 6, -8, -2, 7)

J. Create a tuple containing minimum six students' names. Print the first
student's name.

names = ("Teymur", "Gunel", "Asif", "Rashad", "Elnur", "Samir")
print(names[0])

K. Create a tuple containing three different integers. Print the integer
at position two.

numbers = (2, 9, 54)
print(numbers[1])

L. Print the last element of Task D's tuple.

continents = ("Eurasia", "Africa", "North America", "South America", "Australia", "Antarktida")
print(continents[-1])

M. Print the last two elements of Task A's tuple. You can use slicing
method only once. Separately printing those elements will not be accepted.

colors = ("red", "blue", "green", "white", "brown", "black", "yellow")
print(colors[5:])


N. Given the following tuple:
double_me = (0, 5, 10)

Create a new tuple containing the double value of that tuple.

double_me = (0, 5, 10)
double = (0, 5, 10) * 2
print(double)

O. Create any nested tuple. Print any value from the inner tuple and the whole
inner tuple.

mixed = ("Hello", 3, (54, 75, 2), True)
print(mixed[2][0])
print(mixed[2])

P. Change the value of the color at position six of the tuple from Task A.

elements in tuple are not changeble

Q. From Task B's tuple print all countries except the first two.

countries = ("Azerbaijan", "Georgia", "Germany", "Italy", "Spain")
print(countries[2:])


R. Create two new tuples containing the double value of the tuple from Task F 
using 2 different mathematical operations.

data_types = ("Wolrd", 3, True, [1,3])
new_data = data_types * 2
new_data = data_types + data_types


S. Create an empty tuple.

empty = ()
T. Create a tuple with only the one 'Python' string value. Print its type.

program = ("Value")
print(type(program))

U. Count how many times the word 'hacking' appears in this tuple:
black_hat = ('hacking', 'hiding', 'hiking', 'hacking', 'viking', 'horsing', 'black', 'hat', 'hacking')

print(black_hat.count("hacking"))


V. Count how many 'True's are in this tuple:
booleans = (True, True, False, True, False, False, True)
print(booleans.count(True))

W. Find the position of the first 'a' character in the following tuple:
randomized_alphabet = ('b', 'w', 'v', 't', 'n', 'c', 'd', 'a', 'f', 'a')

print(randomized_alphabet.index('a'))

X. When should you consider using constant variables with tuples in your Python code? 
Provide an example scenario.

when we don't want them to be changeable during the cod's execution
Bonus:
A. Print the whole tuple from previous tasks using the slicing method.

print(colors[:])

B. Print the length of any tuple from previous tasks.

print(len(colors))

- Sets -
You have the following set:
ages = {12, 14, 16, 18, 20, 22, 24, 26}
A. Write a Python program to remove an item from the 'ages' set if
it is present in the set.


ages = {12, 14, 16, 18, 20, 22, 24, 26}
x = float(input("Enter age number:"))
if x in ages:
    ages.remove(x)
print(ages)

B. Add 28 to 'ages' set.

ages = {12, 14, 16, 18, 20, 22, 24, 26}
ages.add(28)
print(ages)

C. Copy this set. Check if this copied set is a subset of the original set.

ages = {12, 14, 16, 18, 20, 22, 24, 26}
ages_copy = ages.copy()
print(ages_copy.issubset(ages))


D. Check if the following set is a subset of the 'ages' set:
suspected_subset = {12, 14}


ages = {12, 14, 16, 18, 20, 22, 24, 26}
suspected_subset = {12, 14}
print(suspected_subset.issubset(ages))



E. Remove 12 and 14 from the 'ages' set.

ages = {12, 14, 16, 18, 20, 22, 24, 26}
ages.remove(12)
ages.remove(14)
print(ages)


F. You have the following tuple and set:

Extend the 'students' set with the 'names'.

names = ('Murad', 'Aysel', 'Gunel')
students = {'Bob', 'John'}
students.update(names)
print(students)



G. Find the difference between the following sets:
fruits = {"apple", "banana", "cherry"}
items = {"google", "microsoft", "apple"}

fruits = {"apple", "banana", "cherry"}
items = {"google", "microsoft", "apple"}
print(fruits.difference(items))

H. Print the length of the 'ages' set. Then add 12 to the 'ages' set. Print the
length again.

ages = {12, 14, 16, 18, 20, 22, 24, 26}
print(len(ages))
ages.add(12)
print(len(ages))


I. Clear the 'ages' set. Print it and its length.

ages = {12, 14, 16, 18, 20, 22, 24, 26}
ages.clear()
print(ages)
print(len(ages))

- Interview Questions -
A. Reverse a tuple with slicing method.

print(colors[::-1])

B. What's the main difference between Tuples and Lists in Python?

tuples are not changeable.

C. What's the best practice to use Sets, and not Lists or Tuples?

Duplicates in sets are not allowed, so when we want to receive the list without duplicates
we can change it to set, and then again to list.
Also when we need to store only unique elements.
When we need to check if any element exist in collection, it will be faster in sets.

D. What's the difference between Set's 'remove' and 'discard' method?

Remowe method return an error, when the removed object doesn't exist, while discard method doesn't

E. You have the following list of the students of 7th grade class:
names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]

How can you remove all duplicate names from this list?

names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]
new_list = []
for x in names:
    if x not in new_list:
        new_list.append(x)
print(new_list)

or

unique_names = list(set(names))
print(unique_names)

F. When might you choose to use a set instead of a list or tuple in Python? 
Provide an example scenario.

Duplicates in sets are not allowed, so when we want to receive the list without duplicates
we can change it to set, and then again to list.
Also when we need to store only unique elements.
When we need to check if any element exist in collection, it will be faster in sets.
With other words, to ensure elements are unique and eliminate duplicates.


- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

- Chat GPT's Homework -
A. Create a Python tuple named student_info that contains the following information about a student:
1. Student's name
2. Student's age
3. Student's grade (as a string, e.g., "A" or "B")

student_info = ("Arzu", 20, "A")

B. Create an empty list called shopping_cart. Then, perform the following operations:
1. Add three items to the shopping cart.
2. Remove one item from the shopping cart.
3. Modify one of the items in the shopping cart.

shopping_cart = ["Butter", "Bread", "Fruits"]
new_items = ["Soap", "Shampoo", "Clothes"]
shopping_cart.extend(new_items)

shopping_cart.pop(1)

shopping_cart[0] = "Pen"

C. Create a tuple named coordinates containing latitude and longitude values. 
Then, use tuple unpacking (*) to assign these values to separate variables called latitude and longitude. 
Print the values of latitude and longitude.

coordinates = (40, 25)
print(*coordinates)

D. Explain in your own words the main differences between tuples and lists in Python.
Provide examples of situations where you would use one over the other.

tuples are unchangeable. Lists are changeable

We use tuples when it is required to protect elements from changes and
when we need to save memory



Quiz.
1. What is a tuple in Python?
    
    b) An ordered collection of elements that is immutable.
   

2. How do you create an empty tuple in Python?
    a) empty_tuple = ()
   

3. Question 3: Which of the following statements is true about sets in Python?
    
    d) Sets are mutable.
    
4. What is the primary purpose of using sets in Python?
    
    b) To ensure elements are unique and eliminate duplicates.
 
5. Which of the following is true about the elements of a set in Python?
    
    d) Elements of a set can be of different data types.
    
6. What is the result of the following code?
    my_set = {1, 2, 3}
    my_set.add(4)
    my_set.remove(2)

    
    b) {1, 3, 4}
    
      

7. Which of the following set operations returns the elements that are common to two sets?
   
    b) intersection()
   

8. Can a tuple contain elements of different data types?
    a) Yes
      
    
9. What is the key difference between a tuple and a list in Python?
    
    b) Lists are ordered and mutable, while tuples are ordered and immutable.
    
    
    
10. Which of the following is a valid way to create a set in Python?
    a) my_set = {1, 2, 3}
   

11. Which of the following statements is true about tuples in Python?
    
    
    c) Tuples can contain duplicate elements.
   

12. What is the advantage of using tuples over lists in Python?
    
    c) Tuples are faster for accessing elements.
  

13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
    a) squared_tuple = (x ** 2 for x in range(1, 6))

    
14. What is the primary advantage of using sets when dealing with collections of data?
 
    c) Sets ensure elements are unique.
   

15. In Python, what would be the result of applying the union() operation on two sets that 
have some overlapping elements?
    
    b) The operation will return all elements from both sets with duplicates removed.
      
    
16. How can you remove an item from a list without knowing its index?
    a) Using the remove() method.
     

17. Which of the following statements is true about list comprehensions?
    a) List comprehensions can only be used with lists.
    b) List comprehensions are faster than for loops for creating lists.
    d) List comprehensions always create a new list.

18. What is the difference between the discard() and remove() methods for sets in Python?
    a) discard() removes an element if it exists; remove() raises an error if the element is not found.
    
    
    
19. In Python, can a list contain elements of different data types?
    a) Yes
   
    
20. In Python, what is a constant variable?
    
  c) A variable whose value should not change after it's initially assigned.
   

21. Which data structure in Python is commonly used to define constant variables?
    
    b) Tuples
    

22. How do you define a constant variable using a tuple in Python?

MY_CONSTANT = ()
 

23. When defining constant variables using tuples, what is the recommended naming convention?

    b) Use uppercase letters with underscores (e.g., MY_CONSTANT_VAR).
  

24. Which of the following operations is valid for a constant variable defined using a tuple?
    
    b) Accessing its elements.
  

25. Why might you choose to use a constant variable defined with a tuple instead of a regular variable?
    
    c) To ensure that the variable's value remains constant.
   

26. Which of the following code examples correctly defines a constant variable using a tuple?
    a) const_var = (3.14, 'hello', True)
   
   

27. What is the advantage of using constant variables with tuples over hardcoding values directly into your code?
    
    c) It saves memory.
    

28. In Python, can you reassign a value to a constant variable defined using a tuple?
    
    Yes

29. What does the asterisk (*) operator do when used with a variable in Python?
    
    c) Allows the variable to hold multiple values, like a list or tuple.
   
30. In Python, what does the from module_name import * statement do when importing a module?
    a) It imports all functions, classes, and variables from the module.
    

31. When might it be appropriate to use the asterisk () in a module import statement?
    
    b) When you want to import all contents of the module for convenience.
    
"""