"""

Lambda functions are annonymous functions that are only used once within the code. They are also called as anonymous functions because they are not declared in the standard manner by using the def keyword. You can use the lambda keyword to create small anonymous functions.

Syntax
lambda arguments : expression

The expression is executed and the result is returned:

Lambda functions are annonymous functions that are only used once within the code.

Lambda can be used with built-in functions like filter(), map() and reduce().
"""

# Example
test_scores = [73, 20, 65, 19, 76, 100, 88]
exam_scores = [12, 4, 9, 14, 16, 19]

# 1: Use lambda on a map to multiply  scores

multiply_scores = list(map(lambda score: score * 2, test_scores))

print('Multiplied Scores', multiply_scores)


# 2: Add multiple list using

add_scores = tuple(map(lambda exam_score, test_score: exam_score +
                       test_score, exam_scores, test_scores))
print('Added Scores', add_scores)

# 3: Get the squared value of the list
items = [5, 4, 3, 2]
squared_list = list(map(lambda item: item**2, items))
print('Squared List', squared_list)

# 4: Use lambda to filter through a list of scores

filter_scores = list(filter(lambda score: score < 50, exam_scores))
print('Filtered Scores =>', filter_scores)


# 5 Sorting list of tuple with lambda

my_list = [(0, 2), (4, 3), (10, -1), (9, 9)]

my_list.sort(key=lambda item: item[1])
print('Sorted List', my_list)
