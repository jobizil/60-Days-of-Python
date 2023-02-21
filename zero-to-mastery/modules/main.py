
import math
from datetime import date

# Custom Module
import my_module

# Importing a package
from mod_list.my_list import list_mod


# Bilt-in modules
x = math.sqrt(25)
print(x)  # Output: 5.0


today = date.today()
print("Today's date:", today)  # Output: Today's date: 2023-02-17

# Custom modules
my_module.greet("Jobizil")  # Output: Hello, Jobizil!

print(my_module.square(5))  # Output: 25
#
# # Packages
names = ["Jobizil", "John", "Jane", "Jill"]
ids = [1, 2, 3, 4, 5, 6, 7]

print(list_mod.find_index(names, 'Jobizil'))
print(list_mod.multiply_list(ids))
