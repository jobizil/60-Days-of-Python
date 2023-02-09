# Definition of List
'''
A list is a collection of items in a particular order.
 You can make a list that includes the letters of the alphabet, the digits from 0-9.
You can put anything you want into a list, and the items in your list don't have to be related in any particular way.
 The syntax for defining a list is to enclose the items in square brackets, with commas between them.
'''

# Example of List and Manipulating it
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])

# Slicing a list => When slicing a list, just as strings, it has 3 parts i.e [start:stop:stepover]
# print(bicycles[1:3])
#  Duplicating a list

# [:] is used to create an entirely new copy of the existing list
""" new_bicycles = bicycles[1::2]
new_bicycles[0] = 'seat'
print(new_bicycles)
print(bicycles) """


# ============================================

# Matrix

# A matrix is a two-dimensional data structure that can store numbers or other types of data ie it's a liat that stores another list inside of them.

# Example of Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[2][0])

#  ============================================

# List Methods
# 1. append() => This method adds an item to the end of the list
# bicycles.append('word')

# 2. insert() => This method adds an item at a specific index
# bicycles.insert(0, 'shoo')

# 3. extend() => This method adds multiple items to the end of the list

# bicycles.extend(['word2', 'word3'])

# 4. remove() => This method removes an item from the list by its value and not by its index
# bicycles.remove('word2')

# 5. pop() => This method removes the last item from the list and returns the popped item

# new_bask = bicycles.pop(0)

# 6. clear() => This method removes all the items from the list and returns an empty list
# bicycles.clear()

# 7. index() => This method returns the index of the first item with the specified value and returns an error if the value is not found

# print(bicycles.index('word3'))

# 8. count() => This method returns the number of times the specified value appears in the list

# print(bicycles.count('word3'))


#  ============================================
#  Common List Patterns
# bicycles.sort()
# bicycles.reverse()
# print(bicycles[::-1]) # This is used to reverse a list and it creates a new copy of the list
# print(bicycles)

#  ============================================

#  List Unpacking
#  This is used to assign multiple variables at once

#  Example of List Unpacking
# a, b, c, *rest, d = bicycles
# print(rest)
# print(d)

#  ============================================
#  Looping through a list
# 1. For Loop
# for bicycle in bicycles:
#     print(bicycle)

# Remove duplicates from a list
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mosh',
         'John', 'Anne', 'Jane', 'Bob', 'Anne']

duplicate_names = []
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)
    else:
        duplicate_names.append(name)

print(unique_names)
print(duplicate_names)


pictures = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in pictures:
    for pixels in row:
        if pixels == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')  # This is used to print a new line after each row


# 2. While Loop
# i = 0
# while i < len(bicycles):
#     print(bicycles[i])
#     i += 1

# 3. Looping through a list of dictionaries
users = [{'username': 'Jobizil',
         'email': 'jobizil@email.com',
          'age': 26},
         {'username': 'Quill',
         'email': 'quill@email.com',
          'age': 22}]

# for user in users:
#     print(user['username'])

#  ============================================
#  List Comprehension
#  This is used to create a new list from an existing list

#  Example of List Comprehension
# new_list = [expression for item in list if conditional]
# new_list = [item['email'] for item in users]
# print(new_list)

#  ============================================
#  List Comprehension with if statement
#  Example of List Comprehension with if statement
new_list = [item['email'] for item in users if item['age'] > 25]
print(new_list)
