def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


def multiply_list(list_of_numbers):
    item = 1
    for number in list_of_numbers:
        item *= number
    return item
