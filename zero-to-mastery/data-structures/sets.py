
# Definition
'''
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
'''

# Example of a set
fruits = {'apple', 'orange', 'apple', 'grape', 'pear', 'banana'}
fruits_2 = {'babana', 'pawpaw', 'apple', 'orange', 'pear', 'banana', 'mango'}
print(fruits)


# # Convert a list to a set
# fruits_list = ['apple', 'orange', 'apple', 'grape', 'pear', 'banana']
# fruits_set = set(fruits_list)
# print(list(fruits_set))

#  ============================================
#  Set Methods
# 1. add() => This method adds an element to the set
# fruits.add('mango')
# print(fruits)

# 2. clear() => This method removes all the elements from the set
# fruits.clear()
# print(fruits)

# 3. copy() => This method returns a copy of the set
# fruits_copy = fruits.copy()
# print(fruits_copy)

# 4. difference() => This method returns a set containing the difference between two or more sets
# print(fruits.difference(fruits_2))
# print(fruits_2.difference(fruits))

# 5. difference_update() => This method removes the items in this set that are also included in another, specified set and returns a set

# print(fruits.difference_update(fruits_2))
# print(fruits)

# 6. discard() => This method removes the specified element from the set
# fruits.discard('apple')
# print(fruits)

# 7. intersection() => This method returns a set that contains the similarity between two or more sets
# print(fruits.intersection(fruits_2))


# 8. intersection_update() => This method removes the items in this set that are not present in other, specified set(s) and returns a set
# print(fruits.intersection_update(fruits_2))

# 9. isdisjoint() => This method returns True if two sets have a null intersection
# print(fruits.isdisjoint(fruits_2))

# 10. issubset() => This method returns True if another set contains this set
print(fruits.issubset(fruits_2))
print(fruits_2.issubset(fruits))

# 11. issuperset() => This method returns True if this set contains another set
print(fruits.issuperset(fruits_2))
print(fruits_2.issuperset(fruits))

# 12. union() => This method returns a set that contains all items from the original set, and all items from the specified sets
print(fruits.union(fruits_2))


# 13. update() => This method updates the current set, by adding items from another set
# fruits.update(fruits_2)
# print(fruits)

#  ============================================
#  Common Set Patterns
# 1. Remove duplicates from a list
# fruits_list = ['apple', 'orange', 'apple', 'grape', 'pear', 'banana']
# fruits_set = set(fruits_list)
# print(list(fruits_set))

# 2. Find the intersection of two lists
# fruits_list = ['apple', 'orange', 'apple', 'grape', 'pear', 'banana']

# fruits_list_2 = ['apple', 'orange', 'apple', 'grape', 'pear', 'banana', 'mango']

# fruits_set = set(fruits_list)
# fruits_set_2 = set(fruits_list_2)

# print(fruits_set.intersection(fruits_set_2))

# 3. Find the difference between two lists

# print(fruits_set.difference(fruits_set_2))
# print(fruits_set_2.difference(fruits_set))

# 4. Find the union of two lists

# print(fruits_set.union(fruits_set_2))
