
# Definition
'''
A tuple is a collection of items in a particular order.
Tuples are immutable, which means you can't modify them after they're created. 
'''
# Example of a tuple
fruits = ('apple', 'orange', 'apple', 'grape', 'pear', 'banana')
# print(fruits[0])
# print(fruits[1:3])
#  ============================================
#  Tuple Methods
# 1. count() => This method returns the number of times a specified value occurs in a tuple
# print(fruits.count('apple'))

# 2. index() => This method returns the index of the first occurrence of a specified value in a tuple
# print(fruits.index('grape'))

#  ============================================
#  Common Tuple Patterns
# 1. Looping through a tuple
# for fruit in fruits:
#     print(fruit)

# 2. Looping through a tuple with index
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

#  ============================================
#  Tuple Unpacking
#  This is used to assign multiple variables at once

#  Example of Tuple Unpacking
a, b, c, *rest, d = fruits
print(rest)
print(d)
