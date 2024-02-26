"""
- Zip (Parallel Iteration) & Enumerate (Counter) -
A. Write a program that takes a list and uses the enumerate method to print each 
element in the list along with its index. Use a suitable formatting for the output.

lst = input("Enter the names and separate them by space:").split()
for index, name in enumerate(lst):
    print(index, name)


B. 
Parallelly iterate over the following collections and print the corresponding
pair values:
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]
for student, gift in zip(students, gifts):
    print(f"{student} has {gift}")

C. Iterate over sequence of fruits and print the order of each fruit:
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]

fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
for num, fruit in enumerate(fruits, start = 1):
    print(num, fruit)


D. Write a program that takes two lists of equal lengths and uses the zip 
method to create a list of tuples, where each tuple contains elements from both 
lists at the corresponding index. Print the resulting list of tuples.

fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
index = [10, 20, 30, 40]
result = tuple(zip(fruits, index))
print(result)


- Date & Time -
A. Write a program that prints 'Running...' each 1.5 seconds. The program should
be terminated after 5 executions of the print statement.

import time
for i in range(5):
    time.sleep(1.5)
    print("Running")


B. Write a program that uses the datetime module to display the current date and 
time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.

import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)


C. Write a program that takes a birthdate (year, month, day) and uses the datetime 
module to calculate the age in years.

import datetime
year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))
day = int(input("Enter the birth day: "))
current_date = datetime.date.today()
age = current_date.year - year - ((current_date.month, current_date.day) < (month, day))
print("The age is:", age, "years")


D. Write a program calculate_elapsed_time(start_time, end_time) that takes two 
datetime objects representing a start time and an end time. Calculate and return 
the elapsed time in hours, minutes, and seconds.

import datetime
start_time = datetime.datetime(2023, 4, 12, 10, 15, 0)
end_time = datetime.datetime(2023, 4, 12, 13, 30, 0)

elapsed_time = end_time - start_time
hours = elapsed_time.seconds // 3600
minutes = (elapsed_time.seconds // 60) % 60
seconds = elapsed_time.seconds % 60

print(f"Elapsed time: {hours} hours, {minutes} minutes, {seconds} seconds")


E. Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
module to determine and return the number of days in that month.

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

days_in_month = calendar.monthrange(year, month)[1]
print(f"The number of days in the specified month is: {days_in_month}")

F. Write a program that takes a birthdate (as a datetime object) and calculates the time 
remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.

import datetime
current_date = datetime.datetime.now()
birthdate = datetime.datetime(1990, 5, 15)

next_birthday = datetime.datetime(current_date.year, birthdate.month, birthdate.day)
if current_date > next_birthday:
    next_birthday = next_birthday.replace(year=current_date.year + 1)


time_until_birthday = next_birthday - current_date
days_remaining = time_until_birthday.days
hours_remaining = time_until_birthday.seconds // 3600
minutes_remaining = (time_until_birthday.seconds % 3600) // 60


while True:
    current_date = datetime.datetime.now()
    time_until_birthday = next_birthday - current_date
    days_remaining = time_until_birthday.days
    hours_remaining = time_until_birthday.seconds // 3600
    minutes_remaining = (time_until_birthday.seconds % 3600) // 60
    print(f"Time remaining until the next birthday: {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes", end='\r')


G. Write a program that uses the time module to display the current time. However, 
add a delay of 5 seconds using time.sleep(5) before displaying the time.

import time
time.sleep(5)
current_time = time.strftime("%H:%M:%S")
print("The current time is:", current_time)

H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
remaining seconds at each interval of 1 second.

import time
seconds = int(input("Enter the time in seconds: "))
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1
print("Time's up!")


I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
to achieve this. The program should display the time at each minute interval.

import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(60)

J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
module to select a random message from a predefined list and display it to the

import random
import time
messages = [
    "Hello, world!",
    "Good morning!",
    "How are you?",
    "Good weather",
    "Stay strong!"
]
while True:
    message = random.choice(messages)
    print(message)
    time.sleep(random.randint(2, 5))

K. Write a program in style of "Squid Game". First, create a list of ten random numbers.
Then, every 10 seconds remove (kill) the smallest value from the list.

import random
import time
numbers = [random.randint(1, 100) for _ in range(10)]
print("Initial list of numbers:", numbers)
while len(numbers) > 0:
    numbers.sort()
    smallest = numbers.pop(0)
    print("Removed", smallest, "from the list. Remaining numbers:", numbers)
    time.sleep(10)



- Chat GPT's Homework -
1. Write a program that uses the zip method to create a new list of tuples,
where each tuple contains elements from both lists at the corresponding 
index.

names = ["Aysel", "Gunel", "Mark"]
index = [1, 2 , 3]
result = tuple(zip(names, index))
print(result)


2. Write a program that takes two lists, keys and values and uses the zip 
method to create a dictionary where the elements from the keys list are the 
keys and the elements from the values list are the corresponding values. 

names = ["Leyla", "Tim", "Mark"]
ages = [25, 40, 24]
students_info = dict(zip(names, ages))
print(students_info)

3. Write a program that takes an iterable and an optional starting index 
(default is 0). Implement the functionality of enumerate using a loop, and 
return a list of tuples where each tuple contains the index (starting from 
the provided start) and the corresponding element from the iterable.

brends_list = ["Chanel", "Versace", "Dior", "Allure", "Egoist"]
for index, name in enumerate(brends_list, start = 20):
    print(index, name)

4. Explain the difference between the time() method and the sleep() method 
in the time module. Provide use cases for each.

time module returns the current time in seconds since the epoch as a floating-point number

sleep() method in the time module suspends execution of the current thread for a specified number of seconds

5. Describe the purpose and functionality of the strftime() method in the 
datetime module. Provide an example of how to use it.

It is used to format a datetime object into a string representation based on a specified format. 


from datetime import datetime
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

6. Explain the significance of the epoch time (January 1, 1970) and how it's 
related to the time() method in the time module.

It represents the number of seconds that have elapsed since 00:00:00 
Coordinated Universal Time (UTC) on January 1, 1970, not counting leap seconds.
 This specific date and time was chosen as the starting point for epoch time 
 due to its historical significance and practicality for computer systems.

7. What is the purpose of the timedelta class in the datetime module? Provide 
an example use case where timedelta can be helpful.

The timedelta class in the datetime module is a built-in class in Python 
that represents a duration or a time interval.
It is used to perform arithmetic operations on date and time values, 
such as adding or subtracting days, hours, minutes, and seconds from a given date or time

Quiz.
1. The datetime module in Python provides a class for manipulating dates 
and times. What is the name of this class?
    a) Datetime
 
2. Which method in the datetime module returns the current date and time?
    
    b) now()
   

3. In the strftime method, what does %Y represent in the formatting string?
    
    b) Year (e.g., 2023)
    
4. Which module in Python provides functionality to work with time-related 
operations such as measuring time intervals, and converting between different 
time representations?
   
    b) datetime


5. Which method from the time module returns the current time in seconds since 
the epoch (January 1, 1970)?
    a) time()
 
6. In the time module, which method pauses the program's execution for the specified 
number of seconds?
    a) sleep()
    


7. Which method of the datetime class in the datetime module returns a formatted string 
representing the date and time?
 
    b) strftime()
   

8. In the datetime module, what does the timedelta class represent?
    a) A duration expressing the difference between two date or time instances


9. Which method of the timedelta class allows you to extract the number of days?
 
    b) total_days()
  
10. To get the current date and time, which method would you use in the datetime module?
    a) datetime.now()
 

11. In the strftime method, what does %d represent in the formatting string?
   
    c) Day of the month (01-31)
  

12. In the strftime method, what does %H represent in the formatting string?
  
    c) Hour (00-23)
   

13. In the strftime method, what does %M represent in the formatting string?
    a) Month (01-12)
   

14. Consider the following Python code snippet:
    import time

    start_time = time.time()
    time.sleep(3)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds.")

    What is the purpose of this code, and what will be the output when it is executed?
    a) This code measures the execution time of the time.sleep(3) statement 
    and prints the elapsed time in seconds.

"""