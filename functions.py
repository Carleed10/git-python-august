# def greet(time_of_day, name="Anonymous"):
#     print(f"Good {time_of_day} {name}")

# greet("morning")


# def add_two_numbers(a, b):
#     return a + b

# print(add_two_numbers(12, 20))

# # raise_to_power

# def greet(name):
#     # no code yet
#     pass


# 2, 5, 7, 11, 12
# 2
# Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0
    
# print(is_even(18))

# 5
# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both 
# numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     if (a % 2 == 0 and b % 2 == 0):
#         return min(a, b)
#     return max(a, b)

# print(lesser_of_two_evens(11, 8))

# 7
# Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name):
#     return name[:3].capitalize() + name[3:].capitalize()


# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# print(old_macdonald("maccarthy"))


# 11
# Write a function upper_lower(text) that accepts a string and calculates the number of uppercase 
# letters and lowercase letters.

# "hello".islower()
# "hello".isupper()

# while loop
# def upper_lower(text):
#     uppercase = 0
#     lowercase = 0

#     i = 0
#     while i < len(text):
#         char = text[i]
#         if char.isupper():
#             uppercase += 1
#         elif char.islower():
#             lowercase += 1
#         i += 1
#     return (uppercase, lowercase)


# no_of_uppercase, no_of_lowercase = upper_lower("Hello**%")
# print(no_of_uppercase)
# print(no_of_lowercase)


# def upper_lower(text):
#     uppercase = 0
#     lowercase = 0

#     for char in text:
#         if char.isupper():
#             uppercase += 1
#         elif char.islower():
#             lowercase += 1
#     return uppercase, lowercase

# no_of_uppercase, no_of_lowercase = upper_lower("HELLO**%")
# print(no_of_uppercase)
# print(no_of_lowercase)


# 12
# Write a function unique_list(list_items) that takes in a list and returns a new list with unique 
# elements of the first list. Do not use the set() constructor.

# [1, 5, 8, 9, 3, 5, 1] => [1, 5, 8, 9, 3]

# def unique_list(list_items):
#     no_duplicates = []

#     for item in list_items:
#         if item not in no_duplicates:
#             no_duplicates.append(item)

#     return no_duplicates

# print(unique_list([1, 5, 8, 9, 3, 5, 1]))


# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# # First call
# print(add_item(1))  # Output: [1]
# # Second call
# print(add_item(2))  # Output: [1, 2]
# # Third call
# print(add_item(3))  # Output: [1, 2, 3]


def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# First call
print(add_item(1))  # Output: [1]
# Second call
print(add_item(2))  # Output: [1, 2]
# Third call
print(add_item(3))  # Output: [1, 2, 3]