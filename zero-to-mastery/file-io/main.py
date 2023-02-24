# Files
'''
File I/O is the process of reading and writing to files to disk storage or your computer  programmatically. There is a high probability that you will need to read and write to files in your Python projects.


# Open a file
To open a file, we use the open() function. The open() function takes two parameters; filename, and mode.

Usually, when a file is opened, it is opened in the same directory as the Python file. However, you can specify the path to the file if it is not in the same directory.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

# Read a file
To read a file, we use the read() method. The read() method returns the whole text, but you can also specify how many characters you want to return.

NOTE: When you are done working with a file, it is a good practice to close it. This can be done by using the close() method.
'''

# my_file = open('sample.txt', 'r')
# print(my_file.name)  # sample.txt
# print(my_file.mode)  # prints mode of file

# my_file.close()

# Read a file
# my_file = open('sample.txt', 'r')
# print(my_file.read())  # prints contents of file
# my_file.close()


# #  Context Manager
# with open('sample.txt', 'r') as file:
#     print(file.read())
#     print(file.read(10))
#     print(file.readline())
#     print(file.readlines())
#     for line in file:
#         print(line, end='')

''' Usually, when usig the context manager, you don't need to close the file. However, if you want to close the file, you can do so by using the close() method. '''

# Write to a file
# with open('sample.txt', 'a') as file:
#     file.write('This is a new line')

# Read a file
''' The read() method returns the whole text, but you can also specify how many characters you want to return.
Also, there is a readline() method that returns one line, and a readlines() method that returns a list of lines in the file.
'''
# with open('sample.txt', 'r') as file:
# print(file.read())  # prints contents of file
# print(file.read(10))  # prints first 10 characters of file
# print(file.readline())  # prints first line of file
# print(file.readlines())  # prints all lines of file as a list
# for line in file:
#     print(line, end='')
# file.seek(0)  # resets the cursor to the beginning of the file
# print(file.tell())  # returns the position of the cursor (in bytes
# print(file.read())

# Append to a file
#  When you append into a  file, the cursor is at the end of the file. So, if you want to append to the beginning of the file, you need to reset the cursor to the beginning of the file.

# with open('sample.txt', 'a') as file:
#     file.write('You could also append to the file. \n')


#  Read and Write to a file
# with open('sample.txt', 'r+') as file:
#     print(file.read())
#     file.write('This is a new line!!')


# Create a file
# with open('new_file.txt', 'w') as file:
#     file.write('This is a new file')


# Exercise:
# Write a program to read a text file and print its contents line by line.

# with open('test.md', 'r') as file:
#     for line in file:
#         print(line, end='')


# Reading contents of a file in chunks
# with open('test.md', 'r') as file:
#     chunk_size = 20
#     content = file.read(chunk_size)
#     while len(content) > 0:
#         print(content, end='')
#         # reads next chunk of file and this continues until the end of the file
#         content = file.read(chunk_size)


# Copying a file

# with open('test.md', 'r') as rf:
#     with open('test_copy.md', 'w') as wf:
#         for line in rf:
#             wf.write(line)


# Copying a file in chunks

# with open('test.md', 'r') as rf:
#     with open('test_copy.md', 'w') as wf:
#         chunk_size = 20
#         content = rf.read(chunk_size)
#         while len(content) > 0:
#             wf.write(content)
#             content = rf.read(chunk_size)
