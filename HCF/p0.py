# Recursive function to return GCD of two number
'''
Repeated Subtraction using Recursion
----------------------------------------

Algorithm
----------
1. Checked whether any of the input is 0 then return sum of both numbers
2. If both input are equal return any of the two numbers
3. If num1 is greater than the num2 then Recursively call findGCD(num1 – num2, num2)
4. Else Recursively call findGCD(num1, num2-num1)

'''





def findGCD(num1, num2):
    
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    
    # base case
    if num1 == num2:
        return num1
    
    # num1>num2
    if num1 > num2:
        return findGCD(num1 - num2, num2)
    else:
        return findGCD(num1, num2 - num1)


num1 = 36
num2 = 60

print("GCD of", num1, "and", num2, "is", findGCD(num1, num2))