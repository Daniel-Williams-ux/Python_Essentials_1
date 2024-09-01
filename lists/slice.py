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
