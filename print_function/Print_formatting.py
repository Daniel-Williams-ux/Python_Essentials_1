# There will be times when you'll want to provide more context to your output than just the  value of a variable. In these instances, you can use what's known as **_print formatting_** to place the value within a larger string.
# Typically, the string will provide more context to the outputted variable.

# To use print formatting, insert the base string inside the print function. Place curly braces where you would like a variable's value to be placed. 
# Add the dot format to the end of the string, with your variables in respective order within the format method, separated by a comma.
# Python will replace the curly braces with the respective variable's value and display the results.

apparatus = "wearable device"
cost = 299

print("The cost of the {} for each participant will be ${}.".format(apparatus, cost))


# or

word_1 = "Often people would first horn their skills in  programming, biology and statistics"
word_2 = "while understanding ethics comes in later when the necessity arises but this would bring long-lasting problems"
print("This stament: {} is a continuation of this: {}".format(word_1, word_2))

# output
# This stament: Often people would first horn their skills in  programming, biology and statistics is a continuation of this: while understanding ethics comes in later when the necessity arises but this would bring long-lasting problems
​
