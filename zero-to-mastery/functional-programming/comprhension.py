# List Comprehnsion
'''
This is used to create a new list from an existing list. It is a more concise way to create a new list from an existing list. It is also more readable and faster than using a for loop to create a new list.
The format is: [param for param in iterable]

Personal disclaimer: I'd suggest you set your list comprehension into a discriptive function

'''

# Example of List Comprehension

my_char = [char for char in 'comprehension']
print(my_char)
numb_range = [num for num in range(0, 26)]  # Prints a list of number from 0-25
num_multiple = [num**2 for num in range(0, 11)]
print(num_multiple)


# Print using Conditions
'''
The format is: [param for param in iterable if condition]
'''


def is_even():
    even_num = [num**2 for num in range(0, 11) if num % 2 == 0]
    return even_num


print('Even Number', is_even())

users = [{'username': 'Jobizil', 'email': 'jobizil@email.com', 'age': 26},
         {'username': 'Lauren', 'email': 'lauren@email.com', 'age': 23},
         {'username': 'Quill', 'email': 'quill@email.com', 'age': 20},
         {'username': 'Luna', 'email': 'luna@email.com', 'age': 15},
         {'username': 'Jane', 'email': 'jane@email.com', 'age': 18}]

# Get users by email
user_email = [item['email'] for item in users]
print('User Email', user_email)

# Get users by age older than 20
user_age = [item['age'] for item in users if item['age'] >= 20]

print('User Age', user_age)


# Dictionary Comprehension
'''
This is used to create a new dictionary from an existing dictionary. It is a more concise way to create a new dictionary from an existing dictionary. It is also more readable and faster than using a for loop to create a new dictionary.
The format is: {key:value for (key,value) in iterable}
'''

# Example

user = {'user1':
        {'username': 'Jobizil',
         'email': 'jobizil@email.com',
         'age': 25,
         'color': 'blue',
         'is_active': True,
         'is_admin': True,
         'is_staff': False},
        'user2':
        {'username': 'Jobizil',
         'email': 'jobizil@email.com',
         'age': 15,
         'color': 'blue',
         'is_active': True,
         'is_admin': True,
         'is_staff': False,
         }}
user_profile = {key: value for key, value in user.items()}


def get_user_by_age():
    profile_age = {key: value
                   for key, value in user.items() if value['age'] < 20}
    return profile_age


print('User Profile', user_profile)
print('Profile Age', get_user_by_age())
