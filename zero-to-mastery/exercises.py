
#  This contains some of the exercises from the zero-to-mastery course

#  1. Write a function that takes a list of numbers and returns the largest number in the list.


def find_largest_number(numbers):

    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(find_largest_number(numbers))


#  2. Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(*args):
        return max(args)

    def best_name(self):
        return f'{self.name} is the best name'


cat_1 = Cat('Tom', 5)
cat_2 = Cat('Jerry', 3)
cat_3 = Cat('Mickey', 7)

oldest_cat = Cat.oldest_cat(cat_1.age, cat_2.age, cat_3.age)

print(f'The oldest cat is {oldest_cat} years old.')


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []

# 3 Instantiate the Pet class with all your cats use variable my_pets

# 4 Output all of the cats walking using the my_pets instance
