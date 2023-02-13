
# Classes
'''Classes are a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.
'''


class User:
    def __init(self, first_name, last_name, username, email, age, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.password = password
        self.is_logged_in = False


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Subclasses

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return f'{self.name} says meow!'

    def __str__(self):
        return f'{self.name} is {self.age} years old and is {self.color}'


class Dog(Pet):
    def speak(self):
        return f'{self.name} says woof!'


cat_1 = Cat('Tom', 5, 'grey')
dog_1 = Dog('Jerry', 3)
print(cat_1.speak())
print(dog_1.speak())
