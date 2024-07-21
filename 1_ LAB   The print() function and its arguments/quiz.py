#Question 1: What is the output of the following program?


print("My\nname\nis\nBond.", end=" ")
print("James Bond.")
 
#output
My
name
is
Bond. James Bond.

#Question 2: What is the output of the following program?


print(sep="&", "fish", "chips")
 
#output
  File "main.py", line 1
    print(sep="&", "fish", "chips")
                  ^
SyntaxError: positional argument follows keyword argument

#Question 3: Which of the following print() function invocations will cause a SyntaxError?

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')
 
output
Line 5 will raise SyntaxError, because the ' symbol in the Greg's book. string requires an escape character.
