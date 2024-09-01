# This code reverses the list my_list by iterating over the first half of the list and swapping each element with its corresponding element from the end of the list.

my_list = [10, 1, 8, 3, 5]

length = len(my_list)       # Define the length

for i in range(length // 2):
  my_list[i], my_list[length - i -1] = my_list[length - i -1], my_list[i]

print(my_list)

# If length is equal to 5, let's walk through how the code would behave:

# Variables:
# my_list: The list you're reversing (e.g., [1, 2, 3, 4, 5]).
# length: Given as 5.
# The for Loop:
# python

# for i in range(length // 2):
# length // 2 is 5 // 2, which equals 2 (since // is integer division).
# This means the loop will iterate twice: i will take the values 0 and 1.
# Iterations and Swapping:
# First Iteration (i = 0):

# The code swaps my_list[0] with my_list[4] (since length - i - 1 equals 5 - 0 - 1 = 4).
# If my_list = [1, 2, 3, 4, 5], after this swap, the list becomes [5, 2, 3, 4, 1].
# Second Iteration (i = 1):

# The code swaps my_list[1] with my_list[3] (since length - i - 1 equals 5 - 1 - 1 = 3).
# After this swap, the list becomes [5, 4, 3, 2, 1].
# Final State of my_list:
# After both iterations, the list is fully reversed:

# Original List: [1, 2, 3, 4, 5]
# Reversed List: [5, 4, 3, 2, 1]
# Summary:
# Even though length is 5 (an odd number), the loop only needs to run length // 2 (which is 2) times. 
#This is enough to reverse the list, as the middle element (3) doesn't need to move. The loop swaps the outer pairs, effectively reversing the list.

# The below code will return every item in a list, starting from the end. In other words, it returns a reversed copy of the list:
states = ["CA", "FL", "TX", "NY", "AZ", "HI", "OR", "NJ"] # ['NJ', 'OR', 'HI', 'AZ', 'NY', 'TX', 'FL', 'CA']

# or

states.reverse()

