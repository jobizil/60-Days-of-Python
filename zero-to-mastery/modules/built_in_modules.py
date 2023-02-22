"""
The Python Built-in Modules are a set of pre-installed modules that come with Python.
"""

# Example
import os
import sys

# Using the random module
'''
This module implements pseudo-random number generators for various distributions.
It is used to generate random numbers for various purposes like generating a random password, selecting a random item from a list, etc.
'''
# # import random
# data = [1, 2, 3, 4, 5, 6, 7]
# print(random.random())
# Output: 0.123456789 (randomly selected float between 0 and 1)
# Output: 5 (randomly selected integer between 1 and 10)
# print(random.randint(1, 10))
# print(random.choice(data))  # Output: 4 (randomly selected from the list)


# Example
# Using the datetime module
'''
The datetime module provides a set of classes to work with dates and times. It is used to get the current date and time, add or subtract days, months, or years, etc. 
'''
# from datetime import date, datetime
# today = date.today()
# tomorrow = date.today() + date.resolution
# yesterday = date.today() - date.resolution
# print("Today's date is:", today)  # Output: Today's date: 2023-02-17
# print("Tomorrow's date is:", tomorrow)  # Output: Tomorrow's date: 2023-02-18
# # Output: Yesterday's date: 2023-02-16
# print("Yesterday's date was:", yesterday)

# Exercise
# Using the datetime module, print the current time and date.
# Hint: Use the datetime module and the now() method.

# today_time = datetime.now()
# current_time = today_time.strftime('%H:%M:%S')  # 24 hour format
# current_date = date.today()
# print(f'Today\'s is {current_date} and the time is {current_time}')
# print(current_time)
# print(current_date)


#  Using the time module
# Exercise
# Using the time module, create a clock that prints the current time every second.

# import time
# while True:
#     localtime = time.localtime()
#     result = time.strftime("%I:%M:%S %p", localtime) # the strftime() method takes two arguments, the format and the time object to format and returns a string representing the time.
#     print(result)
#     time.sleep(1)


#  Using the argv in sys module
'''
The argv module is used to get the command line arguments passed to a script. 
It is also good to note that the first argument is the name of the script. 
i.e. the first argument is the name of the script and the second argument is the first command line argument.
'''

# import sys
# print(sys.argv)  # Output: ['built_in_modules.py']

# Exercise
# Using the argv module, create a script that takes two arguments and prints the sum of the two numbers.

# num_1 = int(sys.argv[1])
# num_2 = int(sys.argv[2])
# sum = (num_1 + num_2)
# print(sum)

#  Using the os module
'''
The os module provides a way of using operating system dependent functionality.
'''
# print(os.getcwd())  # This method returns the current working directory.

# Exercise
# Using the os module, create a script that creates a new directory inside the current directory and also  rename a file in the current directory.
# os.mkdir('new_dir') # This method creates a new directory.
# os.rename('new_dir', 'new_dir_2') # This method renames a file or directory.
