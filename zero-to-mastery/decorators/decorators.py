'''
Decorators are a way to modify or extend the functionality of a class,method or function without changing the source code. Some implementations where decorators are commonly used are logging, caching, authentication and authorization.
Decorators are usually written as functions that takes another function as argument and return a modified version of the original function.'''

# Example of decorators


# def decorator_func(func):
#     def wrapper_func():
#         print(f'This executes before {func.__name__}')
#         return func()
#     return wrapper_func


# @decorator_func
# def greeting():
#     print('You\'re doing well bro')

# greeting()

# #  Another common way decorators are being written is shown below
# def greeting():
#     print('You\'re doing well bro')

# greet = decorator_func(greeting)
# greet()

'''Decorating our functions allows us to easily add extra functionalities to existing function by adding that functionality inside of our wrapper '''


# Decorators with Arguments


# def decorator_func(func):
#     def wrapper_func(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper_func


# @decorator_func
# def user():
#     print('User function called')

# user()


# @decorator_func
# def user_profile(username, email, age):
#     print('This is your profile info: \nUsername:{} \nEmail:{} \nAge:{}'.format(
#         username, email, age))

# user_profile('Jobizil', 'jobizil@email.com', '22')


# Using classes as decorators

# class decorator_class(object):
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         print(f'This executes before {self.func.__name__}')
#         return self.func(*args, **kwargs)


# @decorator_class
# def user():
#     print('User function called')

# user()


# @decorator_class
# def user_profile(username, email, age):
#     print('This is your profile info: \nUsername:{} \nEmail:{} \nAge:{}'.format(
#         username, email, age))

# user_profile('Jobizil', 'jobizil@email.com', '22')


# Other Practical examples

# Using decorators for logging




from functools import wraps
import time
def logger(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        func.__name__), level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args:{args}, and kwargs:{kwargs}')
        return func(*args, **kwargs)
    return wrapper


# @logger
# def user_profile(username, email, age):
#     time.sleep(2)
#     print('This is your profile info: \nUsername:{} \nEmail:{} \nAge:{}'.format(
#         username, email, age))


# user_profile('Jobizil', 'jobizil@email.com', '22')
# Using decorators as timers to determine how long a function took to complete execution

def timer(func):
    from time import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time() - t1
        print(f'{func.__name__} took {t2}s to complete its execution.')
        return result
    return wrapper


# @timer
# def user_profile(username, email, age):
#     time.sleep(2)
#     print('This is your profile info: \nUsername:{} \nEmail:{} \nAge:{}'.format(
#         username, email, age))


#  To stack multiple decorators, we need to import the wraps decorator from the functools module as this helps preserve the original names of the functions.


@timer
@logger
def user_profile(username, email, age):
    time.sleep(2)
    print('This is your profile info: \nUsername:{} \nEmail:{} \nAge:{}'.format(
        username, email, age))


user_profile('Jobizil', 'jobizil@email.com', '22')
