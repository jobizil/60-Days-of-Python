from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_item(li):
    return li.upper()


my_pet = (list(map(capitalize_item, my_pets)))
print(my_pet)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


def sort_zip(items):
    return items


print(tuple(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_pass(item):
    return item > 50


print(list(filter(is_pass, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def my_numbers(a, b):
    return a+b


total = reduce(my_numbers, scores)
print(total)


# 5  Remove duplicates and return unique names from this list using the list comprehension
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mosh',
         'John', 'Anne', 'Jane', 'Bob', 'Anne']

unique_names = list({name for name in names})
print(unique_names)
