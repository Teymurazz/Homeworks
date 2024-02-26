"""
Note. You should use indexing, negative indexing, slicing method,
mathematical operations and other techniques to accomplish tasks.

- Lists -
A. Create a list containing minimum seven different colors.

colors = ["yellow", "green", "red", "blue", "orange", "purple", "black"]

B. Create a list containing minimum five different countries.

countries = ["Germany", "Italy", "France", "Russia", "Turkey"]

C. Create a list containing three string values and two integer values.

lst = ["Hello", "World", "Space", 9, 18]

D. Create a list containing all continents of the world.

continents = ["Eurasia", "Africa", "North America", "Antarktida", "South America", "Australia"]

E. Create a list containing minimum four car brands.

car_brands = ["Mercedes", "Opel", "Volvo", "Volkswagen"]

F. Create a list containing four different data types of Python.

data_types = ["sentence", 9, True, ["yellow", "red"]]

G. Create a list containing only negative even numbers from -2 to -12.

negative_numbers = [-2, -3 ,-4, -5, -6, -7, -8, -9 , -10, -11, -12]

H. Create a list containing only positive even numbers from 0 to 12.

positive_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

I. Combine lists from Task G and H.

combined_numbers = [2, -3 ,-4, -5, -6, -7, -8, -9 , -10, -11, -12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

J. Create a list containing minimum six students' names. Print the first
student's name.

student_names = ["Teymur", "Leyla", "Asif", "Rashad", "Elman", "Konul"]

print(student_names[0])

K. Create a list containing three different integers. Print the integer
at position two.

numbers = [9, 25, 63]
print(numbers[1])

L. Print the last element of Task D's list.

print(continents)

M. Print the last 2 elements of Task A's list. You can use slicing
method only once. Separately printing those elements will not be accepted.

print(colors[5:])


N. Given the following list:
three = [3, 3, 3]

Create a new list containing the triple value of that list.

triple_three = three * 3


O. Create any nested list. Print any value from the inner list and the whole
inner list.

lst = ["yellow", "red", "purple", [1, 5, 9], True]

print(lst[3][2])
print(lst[3])

P. Change the value of the color at position six of the list from Task A.

colors = ["yellow", "green", "red", "blue", "orange", "purple", "black"]
colors[5] = "brown"


Q. From Task B's list print all countries except the first two.

countries = ["Germany", "Italy", "France", "Russia", "Turkey"]
print(countries[2:])


R. Create two new lists containing the double value of the list from Task F 
using 2 different mathematical operations (methods).

data_types = ["sentence", 9, True, ["yellow", "red"]]

double_data_types = data_types * 2
double_data_types data_types + data_types


S. From the following list change the value of the last element to "Bob":
friends = ["Kevin", "Jaren", "Jim", "Carry"]

friends[3] = "Bob"

T. Create an empty list.

lst = []

- Interview Question -
A. Reverse a list with slicing method.

print(lst[::-1])

Bonus:
A. Print the whole list from previous tasks using the slicing method.

print(colors[:])
print(countries[:])
print(continents[:])
print(car_brands[:])
print([data_types[:])
B. Print the length of any list from previous tasks.

print(len(colors))

"""