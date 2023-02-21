

# The reduce() -
# The reduce() function is defined in the functools module. It takes a function and a sequence as arguments, and returns a single value. The reduce() function is useful when you need to apply a function to an iterable and reduce it to a single cumulative value. The function can be found in the functools module and it takes two parameters:
# function : It is a function that is called with two arguments. function has to return a value.
# sequence : It is a sequence like list, tuple, etc.
# The reduce() function returns a single value.
# Reduce is a method for combining an array of values into a single value. Reduce might, for example, be used to sum all the integers in an array or to concatenate all the strings in an array. To use reduce, you must first give a function that instructs reduce on how to combine the data. Two parameters will be supplied to the function: the current value and the next value. The function should return a single value that will be utilized in the reduction.

# Example 1 - Using reduce to sum all the elements in a list
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


# Example 2 - Using reduce to concatenate all the elements in a list
def concat(x, y):
    return x + y


print(reduce(concat, ['a', 'b', 'c', 'd', 'e']))


# Example 3 - Using reduce to find the maximum element in a list
def find_max(x, y):
    return x if x > y else y


# print(reduce(find_max, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Example 4 - Using reduce to find the minimum element in a list


def find_min(x, y):
    return x if x < y else y


# print(reduce(find_min, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


'''

'''
