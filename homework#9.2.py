"""
Note. Add the following list at the top of your code. You will use this list
during the homework in certain tasks:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

Also print the list's modification versions to see the difference.
- List Methods -
A. Make up a formula with built-in python 'len' method that finds helps 
to get the last element from the 'fruits' list.

length = len(fruits)
last_index = length - 1
print(last_index)

B. Add any two fruits to the 'fruits' list.

fruits.append("Watermelone")
fruits.append("Pineapple)

C. Remove third fruit so you can assign it to a variable.

fruits.pop(2)

D. Add a fruit to the 'fruits' list twice, and then print the amount of 
this fruit

fruits.append("Potato")
fruits.append("Potato)
print(fruits.count("Potato"))

in the 'fruits' list.
E. Find the index of 'Grape' object in the 'fruits' list.

print(fruits.index("Grape"))

F. Add 'Avocado' to the 'fruits' list at position four. 

insert.fruits(3, "Avocado")

G. Remove third fruit without getting the removed fruit.

fruits.remove("Orange")

H. Remove a fruit at position one.

fruits.pop(0)

I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop' 
method
by finding its positive index.

fruits.append("Blackberry")
fruits.pop(7)
J. Reverse the 'fruits' list with two different methods. Each time print 
the reversed
list.

print(fruits[::-1])

fruits.reverse()
print(fruits)

K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
list.

fruits.sort()
print(fruits)

L. Suppose you have the following list:
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]

Extend the 'fruits' list with the new list.

full_fruits = fruits.extend(new_fruits)
print(full_fruits)

M. Make a copy of the 'fruits' list. Remove the last three fruits. Print 
both of the
lists ('fruits' and the modified copied version).

fruits_copy = fruits.copy()
fruits_copy = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
fruits_copy = fruits_copy[0:4]
print(fruits_copy)

N. Create a variable named 'occurrence'. Make it equal True if the 
'Papaya' is in the
'fruits' list, otherwise False.

fruits = [""Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]
if "Papaya" is in fruits:
    occurence = True
else:
    occurence = False


O. Clear the 'fruits' list.

fruits.clear()

- Variables -
A. Suppose you have the following variables:
x = 60
y = 70

You need to swap these variables values in one line of code.

x, y = y, x

- ChatGPT's homework (List Methods) -
1. Append and Extend:
a. Write a Python program that creates an empty list and then appends 
the following elements to it: 10, 20, 30, 40, and 50. Print the list 
after each append operation.
numbers = []
numbers.append[10]
print(numbers)
numbers.append[20]
print(numbers)
numbers.append[30]
print(numbers)
numbers.append[40]
print(numbers)
numbers.append[50]
print(numbers)


OR

lst = []
for num in range(10, 51, 10):
    lst.append(num)
    print(lst)

b. Create a second list containing elements [60, 70, 80]. Extend the 
first list using this second list and print the updated list.

elements = [60, 70 ,80]

numbers.extend(elements)
print(elements)

2. Insert and Remove:
a. Write a Python program that creates a list containing the following 

elements: 'apple', 'banana', 'orange', 'grape', 'apple', 'kiwi'.

fruits = ["apple", "banana", "orange", "grape", "apple", "kiwi]

b. Use the 'insert' method to add 'pear' between 'banana' and 'orange' 
in the list. Print the updated list.

fruits.insert(2, "pear)
print(fruits)

c. Use the 'remove' method to remove the first occurrence of 'apple' from 
the list. Print the updated list.

fruits.remove("apple")
print(fruits)

3. Count and Index:
a. Create a list containing the following elements: 2, 4, 6, 8, 4, 10, 4, 
12, 14.

numbers = [2, 4, 6, 8, 4, 10, 4, 12, 14]

b. Use the 'count' method to find how many times the number 4 appears in the 
list and print the count.

print(numbers.count(4))

c. Use the 'index' method to find the index of the first occurrence of 4 in 
the list and print the index.

print(numbers.index(4))

4. Sort and Reverse:
a. Create a list containing the following integers in random order: 45, 23, 
78, 12, 98, 56.

numbers = [45, 23, 78, 12, 98, 56]

b. Use the 'sort' method to sort the list in ascending order and print the 
sorted list.

numbers.sort()
print(numbers)

c. Use the 'reverse' method to reverse the sorted list and print the reversed 
list.

numbers.reverse()
print(numbers)



5. Slice and Concatenate:
a. Create a list containing the following elements: 'red', 'blue', 'green', 
'yellow', 'orange', 'purple'.

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

b. Use slicing to extract a new list that contains only the first three 
colors. Print the new list.

new_colors = colors[0:3]
print(new_colors)

c. Use slicing again to extract a new list that contains the last three 
colors. Print the new list.

new_colors = colors[3:]
print(new_colors)

d. Concatenate the two sliced lists and print the final combined list.

common_colors = colors + new_colors
print(common_colors)
"""