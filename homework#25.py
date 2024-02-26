"""
- Map -
A. Create a function that takes a list of numbers and uses the map() function to 
double each number in the list.

def double_numbers(numbers):
    doubled_numbers = list(map(lambda x: x*2, numbers))
    return doubled_numbers


B. Write a function that takes a list of temperatures in Celsius and uses map() 
to convert them to Fahrenheit using the appropriate conversion formula.

def temperature_convertion(celsius_list):
    fahrenheit_list = ((9 /5 * celsius_list) + 32)
    return fahrenheit_list


celsius_list = [4, 5, 9]
result = list(map(temperature_convertion, celsius_list ))
print(result)



C. Implement a function that takes a list of numbers and uses the map() function to 
calculate the square root of each number.

import math

def root_calculator(nums):
    return math.sqrt(nums)

nums = [4, 9, 16, 25, 36 ,49]
result = list(map(root_calculator, nums))
print(result)

OR

import math

def calculate_square_root(numbers):
    return list(map(lambda x: math.sqrt(x), numbers))

D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".

def format_names(names):
    return list(map(lambda name: f"Hello, {name}!", names))


E. Create a function that takes a list of numbers and uses the map() function to generate a 
power series for each number, up to a specified exponent.

def generate_power_series(numbers, exp):
    power_series = list(map(lambda x: [x**i for i in range(1, exp+1)], numbers))
    return power_series

F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
of the same index from both lists.

def concatenate_lists(list1, list2):
    concatenated_list = list(map(lambda x, y: x + y, list1, list2))
    return concatenated_list

G. Create a function that takes a list of floats and uses the map() function to round each float 
to a specified number of decimal places.

def round_floats(float_list, decimal_places):
    rounded_list = list(map(lambda x: round(x, decimal_places), float_list))
    return rounded_list


H.

def apply_discount(price, discount):
    discounted_list = list(map(lambda x: x - x * discount / 100 , price_list))
    return discounted_list

prices = [100, 200, 300]
discounted_prices = apply_discount(prices, 10)
print(discounted_prices)



I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
a simple encryption algorithm.

def encrypt_sentence(sentence):
    encrypted_sentence = ''.join([chr(ord(char) + 1) if char.isalpha() else char for char in sentence])
    return encrypted_sentence

def encrypt_sentences(sentences):
    return list(map(encrypt_sentence, sentences))


J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.

def count_vowels_in_words(words):
    vowels = 'aeiouAEIOU'
    return list(map(lambda word: sum(1 for letter in word if letter in vowels), words))


K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.

def get_string_lengths(strings):
    return list(map(len, strings))



- Filter -
A. Create a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the even numbers.

def even_list(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
lst = [1, 4, 6, 10, 12, 15]
even_lst = list(filter(even_list, lst))
print(even_lst)


B. Write a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the prime numbers.

def prime_numbers(num):
    k = 0
    for i in range(2, num):
        if num % i == 0:
            k+=1
    if k > 0:
        return False
    else:
        return True
    

lss = [2, 3, 5, 7, 8, 9, 10, 11, 14]
prime_list = list(filter(prime_numbers, lss))
print(prime_list)



C. Implement a function that filters a list of strings to return a new tuple containing 
only the words that are palindromes.

def filter_palindromes(words):
    return tuple(word for word in words if word == word[::-1])

words = ['radar', 'hello', 'level', 'world', 'deified']
palindromes = filter_palindromes(words)
print(palindromes)


D. Given a list of dictionaries representing employees and their salaries, use filter() 
to create a new list of employees whose salary is above a specified threshold.


filtered_employees = list(filter(lambda emp: emp["salary"] > threshold, employees))

print(filtered_employees)


E. Write a function that takes a list of file names and filters it to return a new list 
containing only files with a specified file extension.


def filter_files_by_extension(file_names, extension):
    return [file for file in file_names if file.endswith(extension)]

file_names = ['file1.txt', 'file2.pdf', 'file3.txt', 'file4.doc']
extension = '.txt'
filtered_files = filter_files_by_extension(file_names, extension)
print(filtered_files)



F. Create a function that takes a dictionary of student names and their corresponding grades, 
and uses filter() to return a new dictionary containing only students who passed (grades above 
a certain threshold).

def filter_passed_students(students, threshold):
    passed_students = dict(filter(lambda x: x[1] > threshold, students.items()))
    return passed_students


G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
filters it to return separate lists for each data type.

def filter_data_types(mixed_list):
    int_list = [x for x in mixed_list if isinstance(x, int)]
    str_list = [x for x in mixed_list if isinstance(x, str)]
    float_list = [x for x in mixed_list if isinstance(x, float)]
    
    return int_list, str_list, float_list

H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
of numbers based on the user-provided condition.

condition = input("Enter a condition for filtering the list of numbers: ")
numbers = [1, 5, 10, 15, 20, 25]
filtered_numbers = list(filter(lambda x: eval(str(x) + condition), numbers))

I. Write a function that takes a list of strings and filters it to return a new list containing 
only strings that contain a specific substring.

def filter_strings_by_substring(string_list, substring):
    return [s for s in string_list if substring in s]


J. Implement a function that takes a list of strings and filters it to return a new list containing 
strings with a specified character appearing a certain number of times.

def filter_strings_by_char_count(strings, char, count):
    return [s for s in strings if s.count(char) == count]


K. Create a function that takes a list of integers and uses the filter() function to return a 
new list containing only those numbers for which a specified mathematical function (e.g., square, 
cube) yields a prime result.

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime_results(numbers, func):
    return list(filter(lambda x: is_prime(func(x)), numbers))


L. Write a function that takes a list of date objects and filters it to return a new list containing 
dates within a specified range.

from datetime import datetime

def filter_dates(date_list, start_date, end_date):
    filtered_dates = [date for date in date_list if start_date <= date <= end_date]
    return filtered_dates


M. Given a list of cities and their corresponding countries, use filter() to return a new list 
containing cities from a specific country.

filtered_cities = list(filter(lambda x: x["country"] == specific_country, cities))

print(filtered_cities)


N. Create a function that takes a list of product objects and uses the filter() function to return a 
new list containing only available products.

def filter_available_products(products):
    return list(filter(lambda product: product['availability'] == 'available', products))


O. Implement a function that takes a list and uses filter() to return a new list containing only 
the unique elements.

def get_unique_elements(input_list):
    return list(filter(lambda x: input_list.count(x) == 1, input_list))


P. Write a function that takes a list of words and filters it to return a new list containing only 
anagrams of a specified word.

def find_anagrams(word_list, specified_word):
    specified_word_sorted = sorted(specified_word)
    anagrams_list = [word for word in word_list if sorted(word) == specified_word_sorted]
    return anagrams_list



Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
specified range.

def in_range(num):
    return 50 <= num <= 100

R. Create a function that takes a list of strings and uses filter() to return a new list containing 
only strings that match a specific regular expression.


import re

def filter_strings_by_regex(strings, regex):
    return list(filter(lambda x: re.match(regex, x), strings))



- Reversed -
A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
order of elements in the list.

def reverse_func(lst):
    return list(reversed(lst))


B. Create a function that takes a string and uses reversed() to reverse the characters in the string.

def reverse_str(sentence):
    return "".join(reversed(sentence))


C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.

def reverse_elements(object):
    return tuple(reversed(object))

D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.

def reverse_sentence(sentence):
    sentence = sentence.split()
    return " ".join(reversed(sentence))


E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.

def dictionary_reverse(dict):
    return reversed(dict.items())

F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.


G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.

def reverse_queue(queue):
return list(reversed(queue))

H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.

def reverse_stack(stack):
    return list(reversed(stack))


I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
indices, while keeping the elements at even indices unchanged.

def reverse_odd(lst):
    new_list = []
    for index, char in enumerate(lst):
        if index % 2 != 0:
            new_list.append(char)
    return list(reversed(new_list))

lst = [1, 3, 4, 5]
print(reverse_odd(lst))


J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
separated by a specific delimiter.

- Sorted -
A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in ascending order.

def sort_list(lst):
    return list(sorted(lst))

    
B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in descending order.

def sort_list(lst):
    return sorted(lst, reverse=True)


C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted by their lengths.

def sort_list(lst):
    return sorted(lst, key=len)


D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
the tuples sorted based on their second element.

def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
with its items sorted by their values.

def sort_dictionaries(new_dict):
    return sorted(new_dict.items(), key=lambda item:item[1])

F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted in a case-insensitive manner.

def case_insensitive_sort(string_list):
    return sorted(string_list, key=lambda s: s.lower())


G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
with the objects sorted based on a specified attribute.


H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
with the dates sorted in chronological order.


def sort_dates(date_list):
    sorted_dates = sorted(date_list)
    return sorted_dates

I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
the lists sorted based on the sum of their elements.

def summ_elements(lst):
    return sorted(lst, key=sum)

J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
the integers sorted based on the number of factors they have.

def count_factors(n):
    factor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor_count += 1
    return factor_count

def sort_by_factors(numbers):
    sorted_list = []
    for num in numbers:
        factor_count = count_factors(num)
        sorted_list.append((num, factor_count))
    sorted_list.sort(key=lambda x: x[1])
    sorted_numbers = [num for num, _ in sorted_list]
    return sorted_numbers

K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
the strings sorted based on their last characters.

def sort_strings_by_last_character(strings):
    return sorted(strings, key=lambda x: x[-1])

L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
with the dictionaries sorted based on their keys.

def sort_dictionary(dict):
    return sorted(dict.items())


M. Sort the following list of strings alphabetically by the second letter:
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

def sorted_second_letter(string_list):
    return sorted(string_list, key = lambda x: x[1])

Quiz.
1. What is the purpose of the filter() function in Python?
    A) To remove elements from an iterable based on a given condition
   

2. Which of the following data types can the filter() function be applied to?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above +++

3. What does the filter() function return?
    
    C) A list of filtered elements
    D) A tuple of filtered elements

4. Which parameter does the filter() function take?
    A) A filter function
    B) An iterable
    C) Both A and B
   

5. In the context of the filter() function, what does the filter function do?
    A) Defines the condition for filtering elements
 

6. Which of the following statements is true about the filter() function?
    A) The filter function can only return True or False
 

7. What is the syntax for using the filter() function in Python?
    
    C) filter(function, iterable)
   

8. When using the filter() function, what happens if the filter function returns False for an element?
    A) The element is removed from the iterable
  

9. Can the filter() function be used to filter elements based on multiple conditions?
    A) Yes
    
10. In Python 3, what does the filter() function return by default?
    A) A filter object


11. What is the purpose of the map() function in Python?
    A) To apply a given function to each item in an iterable
  

12. Which of the following is an iterable that can be passed to the map() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above +++

13. What does the map() function return?
    A) A new iterable containing transformed elements


14. What parameters does the map() function take?
    A) A mapping function and an iterable
    

15. In the context of the map() function, what does the mapping function do?
    A) Defines the transformation to be applied to each element
   

16. Which of the following is true about the map() function?
    A) The mapping function can return any data type
 

17. What is the syntax for using the map() function in Python?
  
    C) map(function, iterable)
    

18. When using the map() function, what happens if the mapping function returns None for an element?
   
    B) The element remains unchanged in the iterable


19. Can the map() function be used to transform elements from multiple iterables?
   
    B) No

20. In Python 3, what does the map() function return by default?
    A) A map object
 
21. What is the purpose of the reversed() function in Python?
    A) To reverse the order of elements in an iterable
  

22. Which of the following is an iterable that can be passed to the reversed() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above +++

23. What does the reversed() function return?
    A) A new iterable containing reversed elements

24. What parameter does the reversed() function take?
    A) An iterable


25. In the context of the reversed() function, what does "reversed elements" mean?
    A) The elements are in the opposite order

26. Which of the following is true about the reversed() function?
   
    C) The reversed elements are returned as an iterator
   

27. What is the syntax for using the reversed() function in Python?
    A) reversed(iterable)
    

28. When using the reversed() function, can it be applied to strings?
    A) Yes
    

29. Can the reversed() function be used to reverse a dictionary?
    
    B) No

30. In Python 3, what does the reversed() function return by default?
    A) A reversed object
 

31. What is the purpose of the sorted() function in Python?
    A) To sort elements in an iterable and return a sorted list
 
32. Which of the following is an iterable that can be passed to the sorted() function?
    A) Lists
    B) Strings
    C) Tuples
    D) All of the above +++
    
33. What does the sorted() function return?
    A) A new iterable containing sorted elements
    

34. What parameters does the sorted() function take?
    A) An iterable
   

35. In the context of the sorted() function, what does "sorted elements" mean?
    A) The elements are arranged in ascending order

36. Which of the following is true about the sorted() function?
    
    C) The sorted elements are returned as an iterator


37. What is the syntax for using the sorted() function in Python?
    A) sorted(iterable)
   

38. When using the sorted() function, can you specify a custom sorting order?
    A) Yes, by providing a custom sorting function
 

39. Can the sorted() function be used to sort a dictionary based on its keys or values?
    A) Yes


40. In Python 3, what does the sorted() function return by default?
    A) A list of sorted elements
"""