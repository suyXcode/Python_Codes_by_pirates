# 19.Wap check the no. is prime or not
'''
Algorithm to Check if a Number is Prime
-------------------------------------------

1. Start

2. Input an integer num.

3. If num <= 1, then
       → Print "num is not a prime number".
      → Stop.

4. Otherwise:

         Initialize i = 2

         Set is_prime = True

5.       Repeat while i <= num - 1:

6.              If num % i == 0, then
                      → Set is_prime = False
                      → Break the loop.

7.              Otherwise, increment i by 1.

8.   After the loop:

9.       If is_prime == True → Print "num is a prime number".

10.      Else → Print "num is not a prime number".

11.    End
'''

num = int(input("Enter The int num:"))
if num <= 1:
    print(f"{num} is not a prime number")
else:
    i = 2
    is_prime = True
    while i <= num - 1:
        if num % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
