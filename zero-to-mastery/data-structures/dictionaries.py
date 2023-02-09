# Definition
'''
A dictionary in Python is a collection of key-value pairs usually unordered. Each key is connected to a value, and you can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
'''

# Example of a dictionary
user = {'username': 'Jobizil',
        'email': 'jobizil@email.com',
        'age': 25,
        'color': 'blue',
        'is_active': True,
        'is_admin': True,
        'is_staff': False,
        }

# print(user['username'])

#  ============================================
#  Dictionary Methods
# 1. get() => This method returns the value of the specified key
# print(user.get('username'))

# 2. keys() => This method returns a list of all the keys in the dictionary
# print(user.keys())
# print(user.values())

# 3. items() => This method returns a list of tuples containing the key-value pairs

# print(user.items())

# 4. clear() => This method removes all the items from the dictionary and returns an empty dictionary
# print(user.clear())

# 5. pop() => This method removes the item with the specified key name and returns the value of the removed item

# print(user.pop('username'))

# 6. popitem() => This method removes the last inserted item and returns a tuple containing the key-value pair of the removed item

# print(user.popitem())

# 7. copy() => This method returns a copy of the dictionary

# user_2 = user.copy()
# print(user_2)

# 8. update() => This method updates the dictionary with the specified key-value pairs

# user.update({'username': 'Quill', 'email': 'quill@email.com'})
# user_3 = user.copy()
# print(user_3)


#  ============================================

#  Common Dictionary Patterns
# 1. Looping through a dictionary
""" for key, value in user.items():
    print(f'Key: {key}')
    print(f'Value: {value}') """

# 2. Looping through a dictionary keys
# for key in user.keys():
#     print(key)

# 3. Looping through a dictionary values
# for value in user.values():
#     print(value)


#  ============================================
#  Dictionary Comprehension
# 1. Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# Example of Dictionary Comprehension
# squared = {num: num**2 for num in [1, 2, 3, 4, 5]}
# print(squared)

# 2. Dictionary Comprehension with conditional logic
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# Example of Dictionary Comprehension with conditional logic
# squared = {num: num**2 for num in [1, 2, 3, 4, 5] if num % 2 == 0}
# print(squared)

#  ============================================
