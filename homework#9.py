"""
- Lists -
A. Create an empty list and add 5 user-input integers to it.
my_list = []
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
num_3 = int(input("enter third number:"))
num_4 = int(input("enter fourth number:"))
num_5 = int(input("enter fifth numnber:"))
my_list.extend([num_1, num_2, num_3, num_4, num_5])
print(my_list)

OR

lst = []
integer_str = (input("Enter 5 integer and separate by space:").split())
integer_lst = [int(x) for x in integer_str]
lst.extend(integer_lst)
print(lst)

OR

lst = []
my_lst = [int(input(f"Enter number {x +1} and press 'Enter' after each number:")) for x in range(5)]
lst.extend(my_lst)
print(lst)

B. Take a list of integers as input and print the sum of all the elements in the list.

int_list = input("enter numbers and separate them by space:").split()
new_list = [int(x) for x in int_list]
new_list_summ = sum(new_list)
print(new_list_summ)

C. Ask the user for a sentence and store each word as an element in a list.

sentence = input("Enter any sentence:")
sentence = sentence.split()
print(sentence)

D. Write a program that asks user for six countries. The program should create a list of
those countries and ask for three countries to delete from the list. Make the program
user-friendly, and print each time the content of a list to show the user which countries
are in a list.

countries = input("enter countries separatedd by space:").split()
print(countries)
removed = input("enter countries which you want to delete separated by space:").split()
final_countries = [country for country in countries if country not in removed]
print(final_countries)

E. Which list method makes any list look the same. The lists are the same if its content,
elements and all other properties are the same.

Copy

F. Create an empty list and print its length.
Write a function that accepts a list of names and returns the name with the longest length.

my_list = []

names_list = input("Enter names and separate them by space button:\n").split()
names_list.sort(key=len)
print(f"the name with the longets length is {names_list[-1]}")


G. Ask the user for a list of integers and find the second-largest number in the list. 

numbers_list = input("Please enter numbers and separate them by space button:").split()
new_list = [int(x) for x in numbers_list]
new_list.sort()
print(f"second largest number is {new_list[-2]}")

H. Ask the user for a list of integers and find the mean value of that list.

integers_list = input("Enter integers and separate them with space button:\n").split()
new_list = [int(x) for x in integers_list]
mean_value = sum(new_list) / len(new_list)
print(mean_value)

  
  I. Ask the user for a list of integers and find the third-smallest number in the list.

integers_list = input("Please enter integers and separate them by space button:\n").split()
new_list = [int(x) for x in integers_list]
new_list.sort()
print(f"the third smallest number is {new_list[2]}")

J. Write a program that asks the user for three colors separated by spaces. The
program should print all those colors using comma (you should use string 'join' method). 
For example:
Your colors are red, blue, white.

colors = input("Please enter three colors and separate them by spaces:").split()
new_colors = ",".join(colors)
print(f"your colors are {new_colors}")


K. Write a program that asks the user for four capital cities separated by spaces. 
The program should print all those cities the following structure:
There are many capital cities in the world. For example, Baku, Moscow and Kyiv.

capitals = (input("enter 4 capitals and separate them by space button:")).split()
first_three_cities = capitals[0:3]
last_city = capitals[-1]
first_cities = ",".join(first_three_cities)
print(f"There are many capital cities in the world. For example,{first_cities} and {last_city}")

You should follow all instructions, and not make changes to the structure of final sentence.

L. Take a list of strings as input and sort it in alphabetical order.

sentence = input("Enter any sentence you want:\n")
my_list = sentence.split()
my_list.sort()
print(my_list)


M. Take a list of numeric values as input and sort it in descending order.

numbers = input("Enter values and separate them by space button:\n").split()
new_list = [float(x) for x in numbers]
new_list.sort(reverse=True)
print(new_list)

N. Remove duplicates from a list entered by the user while preserving the original order.

my_list = [1, 1, 2, 2, 2, 3, 4, 4, 5]
list_res = [] 
for x in my_list:
    if x not in list_res:
       list_res.append(x)
print(list_res)

OR

lst = [1, 2, 3, 2, 4, 2, 1, 8, 9, 1]
new_lst = []
[new_lst.append(x) for x in lst if x not in new_lst]
print(new_lst)

OR


lst = [1, 2, 3, 2, 4, 2, 1, 8, 9, 1]
new_lst = list(set(lst))
print(new_lst)

O. Write a program that accepts two lists and concatenates them into a single list.
The first list is a list of fruits, the second is a list of vegetables.

fruits = ["Apple", "Banana"]
vegetables = ["Potato", "Tomatos"]
final_list = fruits + vegetables
print(final_list)

P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.

if len(my_list) > 0:
    print("True")


- List Comprehension -
Suppose you have the following lists:
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]

A. Create a list containing raised to power two values of 'digits' list.

new_digits = [x ** 2 for x in digits]

B. Create a list containing capitalized version of letter values of 'letters' list.

new_letters = [words.capitalize() for words in letters]

C. Create a list containing the 'Comprehension' string value the amount of 'times'
list's length time.

sentence = [input("enter any word") for num in times]

D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
number in the list. The program should print 'True' if that number is negative, and 'False'
otherwise.

import random
lst = [random.randint(-5, 5) for x in range(5)]
lst.sort()
print(lst[1])
if lst[1] < 0:
    print(True)
else:
    print(False)

E. Create a list of 10 random numbers and find the maximum and minimum values.


import random
my_list = [random.randint(0, 10) for _ in range(10)]
my_list.sort()
print(f"maximum value is {my_list[-1]}")   or print(max(my_list))
print(f"minimum value is {my_list[0]}")    or print(min(my_list))


- Comments -
A. One-line comment, if it's appropriate.
B. Multi-line comment, if it's appropriate.

- Chat GPT's Homework -
A. Create a list of colors and write a function that duplicates each color in the 
list. For example, if the list contains "red," it should become ["red", "red"]. 
Print the modified list.

lst = input("enter the colors and separate them by space button:\n").split()
for i in range(len(lst))[::-1]:
    lst.insert(i, lst[i])
print( lst)

OR

colors = ["red", "blue", "green", "yellow"]
duplicated_colors = []
for color in colors:
    duplicated_colors.append(color)
    duplicated_colors.append(color)
print(duplicated_colors)

B. How many methods do you know to create an empty list in Python? 

two

C. Which list method is used to add an element to the end of a list?

append

D. Write a Python code snippet to access the third element in a list named my_list. 

my_list[2]

E. Which list method is used to remove the last element from a list? 

pop

F. What list method is used to insert an element at a specific position? 

insert

G. Write Python code to reverse a list called my_list in-place. 

my_list.reverse()

H. How can you create a shallow copy of a list in Python? 

my_list.copy()

I. Which list method is used to count the number of occurrences of a specific element in a list? 

count

J. Write a Python code snippet to concatenate two lists, list1 and list2. 

list3 = list1 + list2

K. What list method can be used to sort a list in ascending order? 

sort

L. Write Python code to remove the first occurrence of an element 'x' from a list. 

remove("x")

M. Explain the difference between append() and extend() methods when adding elements to a list. 

append is used to add the elements to the end of the list

extend is used to add an another list to the end of the existed list

N. Which list method can be used to remove all elements from a list? 

clear

O. Write Python code to find the index of the first occurrence of an element 'x' in a list. 

list.index("x")

P. What list method can be used to remove and return an element from a specific index in a list?

Pop

Quiz.
1. Which method is used to add an element to the end of a list in Python?
 
    d) append()

2. What is the purpose of the insert() method for lists in Python?
  
    c) Add an element at a specific index in the list.
    

3. Which list method is used to remove and return the last element of a list?
    a) pop()
    

4. What does the extend() method do when used on a list in Python?
    
    b) Adds a new list as elements to the existing list.
    

5. Which list method is used to reverse the order of elements in a list in Python?
    a) reverse()


6. What does the sort() method do when used on a list in Python?
   
    c) Sorts the list in ascending order.
    

7. Which method is used to find the index of the first occurrence of an element in a list?
    a) index()
   

8. What is the purpose of the pop() method when used on a list in Python?
    
    b) Removes and returns the last element of the list.
 

9. How can you count the number of occurrences of a specific element in a list?
    a) Use the count() method.


10. How can you check if a list is empty in Python?
  
    c) Use the len() function and check if it's equal to zero.
   

11. Which method is used to copy the elements of one list to another in Python?
    a) copy()
  

12. How do you remove an element by index from a list in Python?
   
    b) Use the pop() method with the index as an argument.


13. What does the len() method do when applied to a list?

    c) Returns the number of elements in the list
    

14. Given the following list, what is the output of min(my_list)?
    my_list = [0, 2, 4, 1, 5]
    result = min(my_list)

    a) 0
  

15. Given the following list, what is the output of max(my_list)?
    my_list = [0, 2, 4, 1, 5]

   
    d) 5

16. Which list method can be used to find the number of occurrences 
of a specific element in a list?
    a) count()
   

17. What is the output of the following code snippet?
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)

    
    b) [5, 4, 3, 2, 1]
   

18. What is the output of the following code snippet? 
    my_list = [1, 2, 3] 
    my_list.insert(1, 4) 
    print(my_list)
 
    b) [1, 4, 2, 3] 
   

19. Which method is used to remove all elements from a list? 
    a) clear() 
    

20. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = sum(my_list) 
    print(result)

    a) 15 


21. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = my_list.index(3) 
    print(result)

   
    c) 2 

"""