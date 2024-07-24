#Of course, you're always allowed to use parentheses, which can change the natural order of a calculation.
#In accordance with the arithmetic rules, subexpressions in parentheses are always calculated first.
#You can use as many parentheses as you need, and they're often used to improve the readability of an expression, even if they don't change the order of the operations.
#An example of an expression with multiple parentheses is here:

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#Evaluate the modulus operation (%):

25
%
13
25%13
#The modulus operation gives the remainder of the division of 25 by 13:

25
÷
13
=
1
 #remainder 
12
25÷13=1 remainder 12
#Therefore,

25
%
13
=
12
25%13=12
#Add 100 to the result:

12
+
100
=
112
12+100=112
#Multiply the result by 5:

5
×
112
=
560
5×112=560
#Calculate the product of 2 and 13:

2
×
13
=
26
2×13=26
#Divide 560 by 26:

560
÷
26
≈
21.53846153846154
560÷26≈21.53846153846154
#Perform integer division (//) by 2:

21.53846153846154
÷
2
=
10.76923076923077
21.53846153846154÷2=10.76923076923077
#Using the floor division // operator, we discard the decimal part:

10.76923076923077
→
10
10.76923076923077→10
