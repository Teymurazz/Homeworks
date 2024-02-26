"""
Note. Use the with keyword to open and close the file, ensuring proper file handling.

- Working with Files -
A. Write a program to read an entire text file. The name of a file should 
be given by a user.

file_name = input("please enter the file name with it extension:")
with open(f"{file_name}") as file:
    print(file.read())

B. Write a program to read first n lines of a file.

with open ("text.txt") as file:
    n = 5
    for i in range(5):
        line = file.readline()
        print(line)

C. Write a program to read last n lines of a file.

with open("text.txt") as file:
    for i in range(5, 0, -1):
        line = file.readline()
        print(line,end="")


D. Write a program to read a file line by line and store it into a list.
lst = []
with open("text.txt") as file:
    lines = file.readlines()
    for line in lines:
    lst.append(line)
print(lst)
    
E. Write a program to read a file line by line store it into a variable.

file_content = ""
with open("text.txt") as file:
    for line in file:
        file_content+=line


F. Write a python program to find the longest words.

with open("text.txt") as file:
    content = file.read()
all_words = content.split()
max_length = 0
for word in all_words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)
print(f"the longest word in this file is {longest_word}")


G. Write a Python program to count the number of lines in a text file.

with open("text.txt") as file:
    lines = file.readlines()
    num_lines = len(lines)
print(num_lines) 


H. Write a Python program to count the frequency of words in a file.

from collections import Counter
sentence = ""
with open("text.txt") as file:
 for line in file:
  sentence +=line
words = sentence.split()
words_count = Counter(words)
print(words_count)


I. Write a Python program to write a list to a file.

my_list = ["Python", "Java", "C++"]
with open("text.txt", "w") as file:
    for item in my_list:
        file.write(f"\n {item}")


J. Write a Python program to combine each line from first file with the corresponding line in second file.

lst_1 = []
lst_2 = []
with open("text.txt") as file:
    for line in file:
        lst_1.append(line[:-1])
with open("txt2.txt") as file:
    for line in file:
        lst_2.append(line[:-1])
result = dict(zip(lst_1, lst_2))
print(result)


K. Write a program that combines two different file contents with titles ("File No.1", "File No.2")
before the content of each file

with open("text.txt") as file:
    content_1 = file.read()
with open("txt2.txt") as file:
    content_2 = file.read()
combined_content = f"File No.1\n{content_1} \n File No.2{content_2}"
print(combined_content)



L. Write a Python program to read a random line from a file.

import random
with open("text.txt") as file:
    lines = file.readlines()
random_line = random.choice(lines)
print(random_line)


M. Write a Python program to assess if a file is closed or not.

file = open("text.txt")
if file.closed:
    print("File is closed")
else:
    print("File is open. Close it immediately!")


N. Write a Python program to create a file where all letters of English alphabet are listed 
by specified number of letters on each line. Output:
ABC
DEF
GHI
JKL
MNO
PQR
STU
VWX
YZ

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letters_on_line = 3
with open("alphabet.txt", "w") as file:
    for i in range(0, 27, letters_on_line):
        file.write(alphabet[i:i+letters_on_line] + '\n')


O. Suppose you have the following list:
filenames = [
    "bill.pdf",
    "invoice.pdf",
    "registration.pdf",
    "certificate.pdf"
]
Write a program that creates all those files.

filenames = [
    "bill.pdf",
    "invoice.pdf",
    "registration.pdf",
    "certificate.pdf"
]
for name in filenames:
    with open(name, "w") as file:
        print()

- Chat GPT's Homework -
Task 1. Create a text file named "students.txt" with the names of five students, 
one name per line.

with open("students.txt", "w") as file:
    file.write("Gunel\n")
    file.write("Asif\n")
    file.write("Mark\n")
    file.write("Leyla\n")
    file.write("Tim\n")    
   
Task 2. Write a Python program that reads the contents of the "students.txt" file 
using the 'r' mode and prints each student's name on a separate line.

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


Task 3. Add a function to your program that allows the user to input the name of a
new student. Append this name to the "students.txt" file using the 'a' mode. 
Ensure that the name is written on a new line.

with open("students.txt", "a") as file:
    file.write("Seymur \n")

Task 4. Implement a feature that lets the user update a student's name. Ask the 
user to input the old name of the student they want to update and the new name. 
Update the "students.txt" file accordingly. Make sure to handle cases where 
the student's name may appear more than once.

old_name = input("Enter the name which you want to change:")
new_name = input("Enter the new name:")
with open("students.txt" ) as file:
    info = file.read()
    new_info = info.replace(old_name, new_name)
with open("students.txt", "w") as file:
    file.write(new_info)



Task 5.




Task 6. Allow the user to search for a student's name in the list and display 
whether or not the student is present in the file.

name_list = ["Asif", "Gunel","Mark"]
with open("students.txt") as file:
    students_list = file.read()
    for name in name_list:
        if name in students_list:
            print("This name is in list")
        else:
            print("This name is not in list")

Quiz.
1. What is the primary purpose of using the with statement (with context 
manager) when working with files in Python?

    c) To ensure proper file handling by automatically opening and closing the file.
  

2. What are the benefits of using the with statement for file handling in Python?
    
    c) It automatically opens and closes the file.
    

3. What can happen if you don't close files before exiting a Python program?
    a) It can lead to a memory leak.


4. Why is it important to close files after you're done with them in a Python program?
    a) To free up system resources.
    

5. Which file mode is used for reading a file in Python?
    a) 'r'

6. What keyword is used to ensure proper file handling, automatically 
closing the file when done?
   
    c) with
    

7. What mode should you use to open a file for writing, and create a new 
file if it doesn't exist, or truncate the file if it exists?
   
    c) 'w'
   
8. How can you read the entire content of a file and store it as a string in Python?
   
    c) Using the read() method


9. What file mode should you use to add new data to an existing file 
without overwriting its content?
    
    b) 'a'
  

10. Which of the following Python code snippets correctly opens a file 
in read mode, reads its contents line by line, and prints them?
    a
    file = open("data.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
 
11. How can you add a new line of text to an existing file in Python 
without overwriting its existing content?
 
    c) Open the file in 'a' mode and write the new line of text.


12. To update a specific piece of data within an existing file, you should:

    b) Open the file in 'a' mode and append the updated data.


13. Which of the following is a good practice when working with files in Python?
   
    c) Closing files explicitly using the close() method.
   

14. What does the 'x' mode do when opening a file?

    d) Opens the file for exclusive access, but creates a new file if it doesn't exist.

15. What does the following code snippet do?
    with open("file.txt", "w") as file:
        file.write("Hello, World!")

    
    b) Opens the file "file.txt" for writing and overwrites its content with "Hello, World!".
   

16. If you want to read the first 100 characters from a file named "data.txt" 
and store them in a variable, which code snippet should you use?
    a)
    with open("data.txt", "r") as file:
        data = file.read(100)

    

17. What will the following code snippet do?
    with open("file.txt", "a") as file:
        file.write("Line 1\nLine 2\nLine 3")

    
    c) Appends the text "Line 1\nLine 2\nLine 3" as separate lines to the end of the file.
   

18. What is the purpose of the 'b' mode when opening a file in Python?
    a) Opens the file for binary read/write operations.


19. What does the following code snippet do?
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    
    c) Reads all lines from the file "data.txt" and prints them without trailing newline characters.
    

20. What does the following code snippet do?
    with open("grades.txt", "r") as file:
        total = 0
        count = 0
        for line in file:
            grade = int(line.strip())
            total += grade
            count += 1

        average = total / count
        if average >= 90:
            result = "A"
        elif average >= 80:
            result = "B"
        elif average >= 70:
            result = "C"
        else:
            result = "F"
    print("The student's average grade is:", average)
    print("The student's final grade is:", result)

    a) Reads the student's grades from "grades.txt," calculates the 
    average, and prints the average and the corresponding letter grade.
   

21. What does the following code snippet do?
    with open("numbers.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                print(number, "is even.")
            else:
                print(number, "is odd.")

    a) Reads the numbers from "numbers.txt," checks if each number is even 
    or odd, and prints the result for each number.
 

22. What will the following code snippet do?
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "important" in line:
                print(line)

    a) Reads the entire file "data.txt" and prints lines containing 
    the word "important."
 

23. What does the following code snippet do?
    with open("students.txt", "r") as file:
        for line in file:
            if len(line.strip()) > 10:
                print("Long name:", line.strip())
            else:
                print("Short name:", line.strip())

    a) Reads the names of students from "students.txt" and prints "Long name:" 
    for names with more than 10 characters and "Short name:" for names with 10 or fewer characters.
 

24. What is the default file mode used when opening a file in Python if you
don't specify a mode explicitly using the 'r', 'w', 'a', or other mode flags?
    a) 'r' (read mode)
  
"""