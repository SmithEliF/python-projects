# Create a new list from a list

# num_list = [1, 2, 3]

# new_list = [n + 1 for n in num_list]

# print(new_list)

# Create a new list from a string

# name = "Eli"

# new_list = [letter for letter in name]

# print(new_list)

# Create list from range

# my_range = range(1, 5)

# new_list = [n * 2 for n in my_range]

# print(new_list)

# Conditional list comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# new_list = [n for n in names if len(n) <= 4]

# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_list = [n.upper() for n in names if len(n) > 4]

print(new_list)