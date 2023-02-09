
# Definition
'''
An object is an instance of a class. A class is like a blueprint for creating objects. 
A class defines the properties and behaviors that all objects of that class share. 
For example, if you were creating a class called Dog, you might define the properties of a dog to be its name, age, color, and breed. You might also define behaviors, such as walking, sitting, and rolling over. Then, based on that class, you could create individual objects, each of which is a specific instance of that class. For example, you might create a dog named Spot, who is a seven-year-old black Labrador.
'''

# Example of a class with attributes

""" 
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'


# Example of an object with attributes
user_1 = User('Jobizil', 'jobizil@email.com', 25)

print(user_1.name)
print(user_1.email)
print(user_1.greeting()) """

#  ============================================
#  Class Methods
# 1. init() => This method is used to initialize the attributes of an object
# 2. self => This is a reference to the current instance of the class and is used to access variables that belongs to the class
# 3. __init__() => This method is called automatically every time the class is being used to create a new object

#  ============================================
#  Common Class Patterns


# 1. Creating multiple objects &&
# 2. Creating a class method


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):

        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1
        return f'Happy {self.age}th, {self.name}'


# Init user object

# user_1 = User('Jobizil', 'jobizil@email.com', 25)

# print(user_1.age)
# print(user_1.greeting())
# print(user_1.has_birthday())

# 3. Inheritance && # 4. Creating a subclass

class Customer(User):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
        return self.balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init customer object
customer_1 = Customer('Quill', 'quilltech57@gmail.com', 22)
customer_1.set_balance(500)
print(customer_1.greeting())
# 5. Overriding a method


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
