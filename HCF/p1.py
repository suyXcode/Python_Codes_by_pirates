# HCF of Two Numbers
# Here, in this section we will discuss how to find HCF of two numbers in python. HCF means (Highest Common Factor) also known as GCD (Greatest Common Divisor).

# x is called HCF of a & b two conditions :

# 1. x can completely divide both a & b leaving remainder 0
# 2. No other number greater than x can completely divide both a & b
# Linear Quest to find HCF

# Algorithm

# Initialize HCF = 1
# Run a loop in the iteration of (i) between [1, min(num1, num2)]
# Note down the highest number that divides both num1 & num2
# If i satisfies (num1 % i == 0 and num2 % i == 0) then new value of HCF is i
# Print value of HCF

num1 = int(input("Enter the Number :"))
num2 = int(input("Enter the Number :"))

hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)
