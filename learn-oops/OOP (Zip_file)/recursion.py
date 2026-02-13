# It is a progarmming technique where a function calls itself repeatedly until it reaches a base case that stops the iteration.

'''
n = 4
num = 0
for i in range(n,0,-1):
    num = num*10+i
    
for j in range(2,n+1):
    num = num*10 + j
print(num)
'''
# mirror number
'''
n = 4
def mirror_pattern(n):
    if n==1:
        return str(n)
    return str(n) + mirror_pattern(n-1) + str(n)

print(mirror_pattern(6))
'''
# Generate 1 to 10 -
'''
def natural_num(n):
    if n==1:
        print(n)
    else:
        natural_num(n-1)
        print(n)
natural_num(10)
'''
# Natural number with return keyword
'''
def natural_num(n):
    if n<1:
        return 
    natural_num(n-1)
    print(n)
natural_num(10)
'''
# Generate 10 to 1
'''
def natural_num(n):
    if n==1:
        print(n)
    else:
        print(n)
        natural_num(n-1)
natural_num(10)
'''
# Generate table of numbers
'''
def table_num(num,n=10):
    if n==1:
        print(num,"x",n,'=',n*num)
    else:
        table_num(num,n-1)
        print(num,"x",n,'=',n*num)

table_num(10)
'''
# sum of natural number
'''
def sum_natural(n):
    if n==1:
        return 1
    return n + sum_natural(n-1)
print(sum_natural(3))

'''
# sum of squares of natural number
'''
def sum_square(n):
    if n<=0:
        return 0
    return n**2 + sum_square(n-1)

print(sum_square(4))
'''
# sum of cubes of natural number
'''
def sum_square(n):
    if n<=0:
        return 0
    return n**3 + sum_square(n-1)

print(sum_square(4))
'''
# factorial of a number
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(3))

'''
# calculate the power of a given number
'''
num = int(input("Enter a num--"))
pow = int(input("Enter the power--"))
res = 1
for i in range(pow):
    res *= num
print(res)


def power(num,pow):
    if pow <=0:
        return 1
    return num* power(num,pow-1)
print(power(2,0))
'''

# count the digits of a number
'''
def count(num):
    num = abs(num)
    if num == 0:
        return 1  # handle input 0
    if num < 10:
        return 1  # single-digit numbers
    return 1 + count(num // 10)
print(count(0))
print(count(12))
'''
# sum of digits
'''
def sum_digits(num):
    if num == 0:
        return 0
    return num%10 +sum_digits(num//10)
'''

# Reverse a number
'''
def reverse_num(num,res=0):
    if num == 0:
        return res
    res = res*10+num%10
    return  reverse_num(num//10,res)

print(reverse_num(235))
print(reverse_num(10))
print(reverse_num(0))
'''
# palindrome
'''
def palindrome(num):
    num_str = str(num)
    if len(num_str)<=1:
        return True
    elif num_str[0] != num_str[-1]:
        return False
    return palindrome(num_str[1:-1])
print(palindrome(12))
print(palindrome(1221))
print(palindrome(1))

'''

# Greatest number
'''
def greatest_no(lst):
    if len(lst) == 1:
        return lst[0]

    max_rest = greatest_no(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

print(greatest_no((21,32,1,9)))
print(greatest_no((1,0,0.1,1.0)))

def max_val(lst,index=0):
    if index == len(lst)-1:
        return lst[index]
    max_rest = max_val(lst,index +1)
    return  lst[index] if lst[index] > max_rest else max_rest
print(max_val([99.9,10,20,0,12,99.9,6]))

'''
# Fibonacci series nth term 
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
'''
# fibonacci series for n terms
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Num--"))
for i in range(n+1):
    print(fibonacci(i))
'''
# power of 2
'''
n = int(input("Num--"))
i=0
while i!=n:
    if 2**i == n:
        print("2's power",i)
        break
    i+=1
else:
    print("False")


def is_power_of_two(n):
    if n==1:
        return True
    elif n<=0 or n%2 !=0:
        return False
    return is_power_of_two(n//2)
print(is_power_of_two(32))
print(is_power_of_two(30))
print(is_power_of_two(0))
print(is_power_of_two(1))
'''
# POwer of 3
'''
n = int(input("Num--"))
i=0
while 3**i <=n:
    if 3**i ==n :
        print(f"3's power {i}")
        break
    i+=1
else:
    print(False)


def power_of_three(n):
    if n==1:
        return True
    elif n<=0 or n%3 != 0:
        return False
    return power_of_three(n//3)

print(power_of_three(21))
print(power_of_three(81))
print(power_of_three(1))

'''
# ugly no. --> only prime factors are 2,3,5
'''
n = int(input("Num--"))
for i in [2,3,5]:
    while n%i ==0:
        n //=i
        print(n) 
print(n)   
if n == 1:
    print("Ugly no.")
else:
    print("Not")


def is_ugly(n):
    if n==1:
        return True
    if n<=0:
        return False
    if n%2 == 0:
        return is_ugly(n//2)
    elif n%3 == 0:
        return is_ugly(n//3)
    elif n%5 == 0:
        return is_ugly(n//3)

    else:
        return False
    
print(is_ugly(30))
print(is_ugly(16))
print(is_ugly(14))

'''
# Tower of Hanoi
    


# HCF and LCM
'''
a=6
b=15

if a>b :
    min = b
    max = a
else:
    min = a
    max = b

for i in range(min,0,-1):
    if a%i ==0 and b%i ==0:
        print("HCF is : ",i)
        break

lcm = max

while True:
    if lcm%a == 0 and lcm%b == 0:
        print("LCM is : ",lcm)
        break
    lcm +=1


# Recursive function to find HCF
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

# Example
a = 6
b = 12
print("HCF:", hcf(a, b))


def lcm(a, b):
    return abs(a * b) // hcf(a, b)

# Example
print("LCM:", lcm(a, b))



def lcm_recursive(a, b, multiple=None):
    if a==0 or b==0 :
        return 0
    if multiple is None:
        multiple = max(a, b)  # start from the larger number
    
    if multiple % a == 0 and multiple % b == 0:
        return multiple  # Found LCM
    else:
        return lcm_recursive(a, b, multiple + 1)  # Check next number

# Example
a = 6
b = 12
print("LCM:", lcm_recursive(a, b))

'''
# Tower of hanoi

n=5
def hanoi_tower(n,source,target,auxilliary):
    if n==1:
        print(f"move disc-1 from {source} to {target}")
        return

    # move n-1 disks from source to auxillary
    hanoi_tower(n-1,source,auxilliary,target)

    # move nth disk from source to target
    print(f"move disc-{n}  from {source} to {target} ")

    # move n-1 disks from auxillary to target
    hanoi_tower(n-1,auxilliary,target,source)

hanoi_tower(n,'A','C','B')