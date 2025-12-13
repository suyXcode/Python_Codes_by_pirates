'''  Method 1: Using Simple Iteration
Working
In this method we’ll use the concept of loops to repeat the process of breaking down the number and adding it back in the reverse order.

For a given integer variable number we perform the following,

        Run a while loop with the condition number >0.
        Extract the last digit as Remainder using Modulo operator.
        Using the formula reverse = ( reverse * 10 ) + remainder , we keep changing the reverse value.
        Break down the Nunber using divide operator.
        Print the reverse variable.   
'''
num = int(input("Enter a number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(f"Reversed Number: {reverse}")

