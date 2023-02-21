
'''

Generator functions are functions that return a generator object some examples of generator functions are range(), enumerate() etc.
1. range() 
2. enumerate() 
3. yield 
'''
# Example
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


# square_num = square_numbers(num_list)
# print(square_num)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#  The above code is returning a list and it is not memory efficient. We need to use generators to solve this problem.
# def square_numbers(nums):
# for i in nums:
# yield i * i

# square_num = square_numbers(num_list)
# <generator object square_numbers at 0x7f9b8c0b9f50>
# print(square_num)
# print(next(square_num))  # This will return the next value in the generator object until there are no more values to return.
# Instead of returning a list, the above code is returning a generator object. We can iterate over the generator object to get the values one at a time.

#  To get all the values from the generator object, we can use a for loop.
# for num in square_num:
# print(num)  # 1 4 9 16 25 36 49 64 81 100


'''

Exercises:
1. Write a generator function that takes in two numbers (start and end) as parameters and yields all the even numbers between start and end (inclusive).
2. Write a generator function that takes in two numbers (start and end) as parameters and yields all the prime numbers between start and end (inclusive).
'''

# 1. Write a generator function that takes in two numbers (start and end) as parameters and yields all the even numbers between start and end (inclusive).


def even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i


my_even_numbers = even_numbers(1, 50)
for num in my_even_numbers:
    print(num)


# 2. Write a generator function that takes in two numbers (start and end) as parameters and yields all the prime numbers between start and end (inclusive).


def prime_numbers(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                yield i


my_prime_numbers = prime_numbers(1, 50)
for num in my_prime_numbers:
    print(num)


#  Python Generators vs List Comprehension
#  List Comprehension

#  List comprehension is a concise way to create lists in Python. It is a way to create a list in a single line of code. It is a very powerful tool that can be used to create lists in a very efficient way.


#  Example
squares = [i * i for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#  Generators

#  Using a generator function
def square_numbers(nums):
    for i in nums:
        yield i * i


square_num = square_numbers(range(1, 11))
#  print(square_num)  # <generator object square_numbers at 0x7f9b8c0b9f50>
for num in square_num:
    print(num)  # 1 4 9 16 25 36 49 64 81 100

#  Using list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#  Using a generator expression
squares = (i * i for i in range(1, 11))
print(squares)  # <generator object <genexpr> at 0x7f9b8c0b9f50>
