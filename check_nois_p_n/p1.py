# Method 2: Using Nested if-else Statements
# This method uses a nested if-else Statements to check whether a given number is Positive or Negative.

"""
Algorithm
-----------------

This method uses a nested if-else Statements to check whether a given number is Positive or Negative.

Algorithm for the above code is as follows,

1. Initialize num as 15
2. If the num >= 0
        If num == 0 : num is zero
        Else number has to be positive
3. Else the number has to be negative
"""




num = 15
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")