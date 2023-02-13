
# Definition
"""Functional PRogramming is a programming paradigm - a style of building the structure and elements of computer programs - that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data."""
'''
Pure functions are functions that return the same result if given the same arguments, and do not cause any observable side effects.
'''
# Example


# def multiply_by2(items):
#     new_list = []
#     for item in items:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by2([1, 2, 3]))


# Benefits of Pure Functions
'''
1. They are easier to test.
2. They are easier to reason about.
3. They are easier to compose.
4. They are easier to parallelize.
'''

# Immutability
'''
In functional programming, immutability is the absence of state change over time. If a program is stateless, then it's output is only determined by its input.
'''

# Example

# a = 2
# b = a
# print(a)
# print(b)
# a = 3
# print(a)
# print(b)

# Example 2
# my_list = [1, 2, 3]
# my_list_copy = my_list
# print(my_list)
# print(my_list_copy)

# my_list.append(4)

# print(my_list)
# print(my_list_copy)

"""The first example shows that the variable b is a copy of a. The second example shows that the variable my_list_copy is a reference to my_list. This is because lists are mutable. If we want to make a copy of a list, we can use the list() function.
"""

# Built-in Functions
'''Some built-in functions that return new lists are: map(), filter(), and zip(). These functions do not change the original list.
'''
"""
- The map() function applies a function to every item in an iterable and returns a new iterable with the results.
The map() function takes two parameters:
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

It is good to know that the map function separates the function from the data(iterable) which is a very important concept in functional programming.


"""

# Example 1 - Using map on a list to get the double of each element
""" 
my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def myltiplyElement(li):
    return li * 2


mapped_list = map(myltiplyElement, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(mapped_list))
# print(tuple(mapped_list))
# print(set(mapped_list))
 """

# Example 2 - Using map on a set to get the length of each element
""" 
def get_length(item):
    return len(item)


length_of_element = map(
    get_length, {'apple', 'banana', 'orange', 'apple', 'mango'})
print(list(length_of_element))
 """
# Example 3 - Using map on a dictionary to get the length of each key
""" 

def item_length(item):
    return len(item)


length_of_key = map(item_length, {'apple': 1, 'banana': 2, 'orange': 3})
print(list(length_of_key))
 """

# The filter() function creates a new list with only the items that return true when passed into a function.
# Just like the map function, the filter() function takes two parameters:
# fun : It is a function to which filter passes each element of given iterable.
# iter : It is a iterable which is to be filtered.

# Example

my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(item):
    return item % 2 == 0


even_list = filter(is_even, my_list)
# print(list(even_list))


# The zip() function ta kes iterables (can be zero or more), aggregates them in a tuple, and return it.
# The syntax of zip() is:
# zip(*iterables) : This function takes iterables as arguments and returns an iterator. The returned iterator generates a series of tuples containing elements from each iterable. The iterator stops when the shortest input iterable is exhausted.
# Example

username = ['john', 'jane', 'joe', 'josh']
email = ['john@email.com', 'jane@email.com', 'joe@email.com']

print(set(zip(username, email)))


# Example 2

names = ['john', 'jane', 'joe', 'josh']
ages = [23, 24, 25, 26]
heights = [180, 175, 178, 182]

print(list(zip(names, ages, heights)))
