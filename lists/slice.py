# [1:3] simply means [start:end(excluding the last index of the end)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) # [8, 6]

# this copies the entire list
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list) # [10, 8, 6, 4, 2]

# starting from index 1 = 8 and minus the last index

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # [8, 6, 4]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) # []

# If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
# my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) # [10, 8, 6]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) # [4, 2]


my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) # [10, 4, 2]

# Deleting all the elements at once is possible too:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) # []

# Removing the slice from the code changes its meaning dramatically.
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) # The del instruction will delete the list itself, not its content.
# The print() function invocation from the last line of the code will then cause a runtime error.


# The in and not in operators
# Python offers two very powerful operators, able to look through the list in order to check whether a specific value is stored inside the list or not.
# These operators are:
# elem in my_list
# elem not in my_list

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
# False
# True
# True


# Scenario
# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue.
# We don't want any repetitions. We want them to be removed.

# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

# Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry 
# out a conversation with the user and obtain all the data from her/him.

# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

# We've provided no test data, as that would be too easy. You can use our skeleton instead.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Create an empty list to store the unique elements
unique_list = []

# Iterate over each element in the original list
for item in my_list:
    # If the element is not already in the unique list, add it
    if item not in unique_list:
        unique_list.append(item)

# Print the list with duplicates removed
print(unique_list) # [1, 2, 4, 6, 9]


