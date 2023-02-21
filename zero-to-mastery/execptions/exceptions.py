'''

Exceptions in Python are errors that occur during the execution of a program. They are used to indicate that something has gone wrong and can be handled by the program to prevent it from crashing.
An exception is a description of what went wrong and a tracebact to where it happenned.


# Common Exceptions: Some of the most common exceptions are:
# 1. ZeroDivisionError
# 2. NameError
# 3. TypeError
# 4. IndexError
# 5. KeyError
# 6. AttributeError
# 7. ValueError
# 8. SyntaxError
# 9. IndentationError
# 10. ModuleNotFoundError

'''
# Examples of common exceptions
# 1. ZeroDivisionError
# print(1/0)

# 2. NameError
# print(age)

# 3. TypeError
# print('1' + 1)

# 4. IndexError
# fruits = ['Apple', 'Orange']

# print(fruits[2])

# 5. KeyError
# fruits = {'Apple': 1, 'Orange': 2}
# print(fruits['Banana'])

# 6. AttributeError
# fruits = ['Apple', 'Orange']
# fruits.append(1)
# print(fruits)

# 7. ValueError
# int('a')

# 8. SyntaxError
# print('Hello)

# 9. IndentationError
# def greet():
# print('Hello')

# greet()

# 10. ModuleNotFoundError
# import module


# Raising Exceptions: You can raise exceptions by using the raise keyword. You can also raise exceptions with a custom error message.
# raise Exception('This is an error message')


'''
# Handling Exceptions => Handling exceptions is a way to prevent your program from crashing when an exception occurs. You can handle exceptions by using the try and except keywords. The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try- and except blocks.
# try:
#     # code that might throw an exception
# except:
#     # code that runs if an exception is thrown
# else:
#     # code that runs if no exception is thrown
# finally:
#     # code that runs no matter what
'''

# Examples on Handling Exceptions

# while True:
#     try:
#         age = int(input('Input your age: '))
#         print(10/age)
#     except ValueError:
#         print('Please enter a valid number')
#     except ZeroDivisionError:
#         print('Please enter an age higher than 0')
#     else:
#         break

# Error Handling in functions


def divide(dividend, divisor):
    '''Divides two numbers and returns the result.'''
    try:
        print(type(dividend), type(divisor))
    except ZeroDivisionError as error:
        return error
    except TypeError as error:
        return error
    else:
        return dividend/divisor
    # finally:
    #     return 'This is the finally block'


print(divide(101, 10))
# print(divide(1, 'a'))


# Exercise
# # 1. Write a function that reads the content of a file  and measure the time it takes to read the file.


# import logging
# import time
# logging.basicConfig(filename='exceptions.log', level=logging.DEBUG)
# logger = logging.getLogger()


# def read_file(path):
#     '''Reads the content of a file and measure the time it takes to read the file.'''
#     start = time.time()
#     try:
#         time.sleep(2)
#         file = open(path)
#         data = file.read()
#         return data

#     except FileNotFoundError as error:
#         logger.error(error)
#         raise
#     else:
#         file.close()

#     finally:
#         end = time.time()
#         time_difference = end - start
#         logger.info((f'Time taken to read file: {time_difference}s'))


# data = read_file('sample.txt')

# print(data)
