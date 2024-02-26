"""
Note. Use clear and descriptive variable names throughout the code.
Make sure to add comments to explain the purpose and functionality of 
your code.

- String Formattings -
A. Create a variable called 'genre'. Give it a string value.              # genre = "Hard Rock"
B. Create a variable called 'producer'. Give it a string value.           # producer = "Steven Spielberg"
C. Create a variable called 'song'. Give it a string value.               # song = "Die Sonne"
D. Using three Python String Formatting types (f-strings, .format(), %s) 
create 3 variables accordingly to the formats count, and make it equal 
to little text (story) using all variables from Task A to C.

sentence = f"My lovely genre of music is {genre}.The best producer in the world is {producer}.
My lovely song is {song} by Rammstein." # f-string

sentence = "My lovely genre of music is {}.The best producer in the world is {}.
My lovely song is {} by Rammstein.".format(genre,producer,song)   # format()

sentence = "My lovely genre of music is %s.The best producer in the world is %s.
My lovely song is %s by Rammstein. %(genre,producer,song)   # %s


E. Create a variable called 'firstname'. Give it an appropriate value.  # first_name = "John"
F. Create a variable called 'lastname'. Give it an appropriate value.   # last_name = "Johns"
G. Create a variable called 'age'. Give it an appropriate value.        # age = 35
H. Create a variable called 'gender'. Give it an appropriate value.     # gender = "Male"
I. Using all of string formatting methods and variables from Task E to H, 
print as the following:
My name is John Smith, and I am 27 years old. My gender is - Male.

sentence = f"My name is {first_name} {last_name}, and I am {age} years old. My gender is - {gender}."          # f-strings
sentence = "My name is {} {}, and I am {} years old. My gender is - {}.".format(first_name,last_name,age,gender) # format()
sentence = "My name is %s %s, and I am %s years old. My gender is - %s." %(firstname,lastname,age,gender)   # %s




J. Create a variable called 'language'. Make it equal 'Python'. Using f-strings
print 'I love Python. I will repeat this word 5 times: PythonPythonPythonPythonPython.'

language = "Python"
print(f"I love {language}. I will repeat this word 5 times: {language * 5}")


K. Create a variable called 'hello'. Make it equal 'Hello'.
Create a variable called 'world'. Make it equal 'World'. 
Using math operations and '.format' string-formatting method print 'Hello World!'.

hello = "Hello"
world = "World"
print("{a} {b}!").format(a=hello,b=world)

L. Create a variable called 'hello'. Make it equal the date of your birthday in
the following format => "01.01.2001". Using '%s' string-formatting method print
the following:
My birth date is 01.01.2001.

hello = "01.01.2001"

print("My birth date is %s" %(hello))


M. Create a text-story using all variables created through all tasks in this
homework file. You should use multi-line strings.

"""I learn Python, and for today our homework was to make variables,
   that called genre, producere and song name. When I've come to the task
   about firstname and lastname, I've written John Johns, and set the age
   of 35 for him. And, of course, his gender was Male. That was all, what 
   I can say. Thanks for attention""""


N. Create a variable with a string value that will contain 4 curly brackets 
(you will fill them soon). Additionally, create 4 different variables of any type 
on your own. Using '.format' string-formatting method and those 4 variables fill 
the previous string with 4 curly brackets. Print it.

sentence = "My friend works as an {}.He is {} years old.He lives in {}.He likes to {} a lot"

job = "engineer"

age = "35"

city = "Baku"

hobby = "travel"

print("My friend works as an {}.He is {} years old.He lives in {}.He likes to {} a lot".format(job,age,city,hobby))





O. Perform math operations with strings in a 'f-string' string-formatting method.

name = "John"

age = 25

sentence = f"My colleague's name is {name}. He is {age * 2} years old."



P. Create a variable called 'expression'. Give it any string value.
Using a variable which you have created previously and contains 4 curly brackets
print the 'expression's value 4 times using '.format' string-formatting method.


sentence = "{}{}{}{}"

expression = "Python is the best!"

print(sentence.format(expression, expression, expression, expression))


Quiz:
A. In the following code, 'Hello' is a string literal. True or false?

    ---------------------
    |    s = 'Hello'    | 
    ---------------------

    a) True
  

B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
    a) Yes
   

C. Is there a problem in the code below? If yes, then how can we rectify it?

    ------------------------------
    |    s = 'Python's call!'    | 
    ------------------------------

    
    b) Yes, by using a backslash
  

D. How to denote a multiline string in Python?
    a) Using ''' '''
    b) Using """ """
    c) Using either (b) and (c) +++++++

E. When used on strings, what does the * operator do?
    a) Replicates them
   