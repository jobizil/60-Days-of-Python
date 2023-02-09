
# Definition

''' A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.'''

# Example of a function


def extract_duplicate_names(names):
    duplicate_names = []
    unique_names = []

    for name in names:
        if name not in unique_names:
            unique_names.append(name)
        else:
            duplicate_names.append(name)
    print(duplicate_names)


names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mosh',
         'John', 'Anne', 'Jane', 'Bob', 'Anne']

fruits = ('apple', 'orange', 'apple', 'grape', 'pear', 'banana')

extract_duplicate_names(names)
extract_duplicate_names(fruits)

#  ============================================
#  Function Parameters
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Parameters
# 4. Variable Length Arguments
# 5. Variable Length Keyword Arguments

#  ============================================
#  1. Positional Arguments
#  This is the most common way to pass arguments to a function
#  The order of the arguments matters

#  Example of a function with positional arguments


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!\nWelcome aboard!')


greet_user('John', 'Smith')


#  2. Keyword Arguments
#  This is used to pass arguments to a function in any order

#  Example of a function with keyword arguments


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!\nWelcome ✒︎')


greet_user(last_name='Doe', first_name='Jane')


#  3. Default Parameters
#  This is used to assign a default value to a parameter

#  Example of a function with default parameters

def greet_user(first_name, last_name='Doe'):
    print(f'Hi {first_name} {last_name}!\nWelcome 🫥')


greet_user('John', 'Wick')


#  4. Variable Length Arguments (args)
#  This is used to pass a variable number of arguments to a function

#  Example of a function with variable length arguments


def multiply(*args):
    total = 1
    for number in args:
        total *= number
    print(total)


multiply(2, 3, 4, 5)


#  5. Variable Length Keyword Arguments
#  This is used to pass a variable number of keyword arguments to a function

#  Example of a function with variable length keyword arguments


def save_user(**user):
    print(user)


save_user(id=1, name='John', age=22)


#  ============================================
