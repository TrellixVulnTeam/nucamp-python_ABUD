"""
the (4) primitive data types: string, integer, float, boolean
"""

name = "Eric"
age = 27
cash = 420.69
sexy = True


# print("The data type for variable 'name' is:", type(name)) # >> string
# print("The data type for variable 'age' is:", type(age)) # >> integer
# print("The data type for variable 'cash' is:", type(cash)) # >> float
# print("The data type for variable 'sexy' is:", type(sexy)) # >> Boolean


"""
the (4) composite data types: list, dictionary, tuple, set
"""

# Data composed as a `List`; ordered sequence of multiple values
nucamp_locations = ["Seattled", "Tacoma", "Bellevue"]

# Data composed as a `Dictionary`; unordered collection of key-value pairs; equivalent to an array
Eric_Info = {"name": "Eric", "age": 27, "cash": 420.69, "sexy": True}

# Data composed as a `Tuple`; similiar to a list, but immutable
my_cool_tuple = ["apple", "bannana", "cherry"]

# Data composed as a `Set`; unordered collection of values, immutable, no duplicate values
my_cool_set = {"cats", "dogs", "bridges"}

print("The data type for variable 'nucamp_locations' is:",
      type(nucamp_locations))  # >> list
print("The data type for variable 'Eric_Info' is:",
      type(Eric_Info))  # >> dictionary
print("The data type for variable 'my_cool_tuple' is:",
      type(my_cool_tuple))  # >> tuple
print("The data type for variable 'my_cool_set' is:", type(my_cool_set))  # >> set
