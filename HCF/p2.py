#Repeated Subtraction with Modulo Operator using Recursion
'''
Algorithm
------------
If b is equals to 0 return a
Else recursively call the function for value b, a%b and return 

'''
# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in euclidean algorithm

def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


num1 = 36
num2 = 60

print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))