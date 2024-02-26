"""
- Strings -
A. Create a variable called 'long_sentence'. Make it equal a sentence
minimum. Print 'long_sentence's length.     

long_sentence = "sentence minimum"
print(len(long_sentence))


B. Replace Print function's 'end' parameter from default '\n' to '\t'.
Write 2 Print functions with it.

print("Hello World", end = '\t')


C. Change Print function's 'end' parameter, so that it links values with
stars. Example:
Today*is*a*good*day!

print("Today", end = '*')
print("is", end = '*')
print("a",end = '*')
print("good", end = '*')
print("day!")





D. Write 3 different Print functions with according string ("He", "is", "cool.")
in such way so you can see this on your console (you can use any method):
He is cool.

print("he","is","cool")
print("he is cool")

print("he",end = ' ')
print("is",end = ' ')
print("cool")




E. The same task as previous (D), but now make it look like:
He#is#cool.

print("He","is","cool", sep='#')
print("He#is#cool")

print("He",end = '#')
print("is",end = '#')
print("cool")


F. Create a variable named 'color'. Give it a string 'Python' value.       # color = "Python"
G. Create a variable named 'item'. Give it a string 'Developer' value.     # item = "Developer"
H. Use all methods you know about string-formattings and Print function
to concatenate these two variables, so you can see 'Python Developer' on your
console (terminal).

color = "Python"
item = "Developer"
print(f"{color} {item}")
print("{a} {b}".format(a=color,b=item))
print("%s %s" %(color,item))


I. Replace Print function's 'end' parameter from default value to '...'.
Write 3 Print functions with it.

print("I like Python", end = '...')
print("Python is the best", end = '...')
print("I learn Python", end = '...')


J. Suppose you have the following variable:
word = "Hello. I am Taylor."

Using slicing method:
1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.

prefix = word[0:6]

2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.

middle_part = word[7:11]

3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.

name = word[12:]

Create a variable named 'recreated_word' or 'result' and use all previous variables 
(prefix, middle_part, name) to recreate the 'word' phrase.

result = f"{prefix} {middle_part} {name}"

K. Suppose you have the following value:
"abababababa"

Using slicing method, get all 'a' characters from the value and assign it to a
variable, then print that variable.

a = "abababababa"
n = a.count("a")
print(n)


L. Create a formula that finds the last index of a string.

last_index = len - 1


M. What is the difference between 1 and "1"? Are they equal values, why?

not equal, because 1 - is a number, "1" is a string. There are different types of variables.

N. Using all your Python knowledge, find the amount of words the following sentence:
"The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."

sentence = "The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."

space_count = sentence.count(" ")

word_number = space_count + 1

print(word_number)

- String Methods -
A. Use all these string methods and test it in your code:
1. title
2. capitalize
3. count
4. endswith
5. find
6. index
7. isalpha
8. isdigit
9. islower
10. isupper
11. lower
12. upper
13. replace
14. split
15. strip
16. startswith
17. join

print(sentence.title())
print(sentence.capitalize())
print(sentence.count("Python"))
print(sentence.endswith("!"))
print(sentence.find("language"))
print(sentence.index("Python"))
print(sentence.isalpha())       # it gives False.Why?
print(sentence.isdigit())
print(sentence.isupper())
print(sentence.islower())
print(sentence.lower())
print(sentence.upper())
print(sentence.replace('Python', 'C++'))
print(sentence.split())
print(sentence.strip())
print(sentence.startswith("888"))
print(sentence.join("/"))

B. Combine several string methods at once.

print(sentence.replace('Python', 'C++'))
print(sentence.split())
print(sentence.strip())
print(sentence.startswith("888"))

C. Create any string-valued variable. First, call the 'lower' method on it,
then call 'islower' method. What value will it always give you and why?

sentence = "I LOVE PYTHON"
print(sentence.lower())
print(sentence.islower())

it gives False value because there is not defined variable according it


D. Suppose you have the following variable:
my_value = "Obviously, today is a hot day."
Replace all 'o' characters with 0 (zeros). 

print(my_value.replace("o","0"))

E. Count how many times the word 'likes' occured in the following string:
"Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."

sentence = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."

print(sentence.count("likes"))

- String Formattings -
A. Create a variable 'name' and assign your name to it.
Create a variable 'age' and assign your age to it.
Using the f-string method, create a formatted string that displays your name 
and age in the following format:
"My name is [name] and I am [age] years old."

name = "Teymuraz"
age = 39
sentence = f"My name is {name} and I am {age} years old."

B. Create a variable item and assign a string representing an item name.
Create a variable quantity and assign an integer representing the quantity of the item.
Create a formatted string using the old-style % formatting that displays the item 
name and quantity in the following format:
"I want to buy %d units of %s."

item_name = "notebook"
quantity = 1

sentence = "I want to buy %s units of %s" %(quantity,item_name)

C. Make your best and create a hard task by your own using string formattings.

sport = "Tennis"
job = "Developer"
age = 40
sentence = f"My favourite sport is {sport}.I'm a {job}.I'm {age} years old"
sentence = "My favourite sport is {}.I'm a {}.I'm {} years old".format(sport,job,age)
sentence = "My favourote sport is %s.I'm a %s.I'm %s years old" %(sport,job,age)

- Chat GPT's Homework -
A. Use the len() function to find the length of the following strings:
1. "programming"    print(len("programming"))
2. "python is fun"  print(len("python is fun))
3. "12345"          print(len("12345))
B. Convert the following string to uppercase string:
"hello world" 

sentence = "hello world"
print(sentence.uppercase())
C. Check if the string "python" is present in the following sentence:
"I enjoy programming in Python."   

print(sentence.find("python"))


D. Given the string "programming", access the following elements using positive and negative indexing:
1. The first character    print(word[0])    print(word[-11])
2. The last character     print(word[[10]]) print(word[-1])
3. The third character    print(word[2])     print(word[-9])
4. The second-to-last character         print(word[1:])
E. Using string slicing, extract the word "is" from the string:
"Python is a versatile programming language."      print(word[7:9]) 
F. Retrieve the substring "quick brown" from the following sentence:
"The quick brown fox jumps over the lazy dog."     print(word[4:15])
G. Reverse the following string using slicing:
"redivider"    print(word.[::-1])    
H. Write a program that capitalizes the first letter of each word in the following sentence:
"welcome to the world of programming"
print(sentence.title())

- Interview Questions -
A. Reverse any string using slicing method.  print(sentence.[::-1])

B. Print the whole string using slicing method, not knowing the length of a string.
print(sentence.[0:])

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz:
A. What does len('Hello ') return?
   
    c) 6
  

B. What is the output of the following code snippet:

    sphere = "Web Development" * 2 + "" * 6
    length = len(sphere)
    print(length)

   
    d) 30

C. Which of the operator can be used in Strings?
    a) +
    b) *
    c) Both of the above
    

D. What is the output of the following code snippet:

    comment = "I like your blue pants"
    pattern = comment[19:4:-3]
    print(pattern, len(pattern))

    a) "n lry", 5
  

E. Is the following variable named correctly, why?

    myVariable = "Python is best!"

    
    b) no, doesn't follow the rules of naming a variable, non-pythonic code
    
"""