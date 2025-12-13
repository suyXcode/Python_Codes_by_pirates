# While Loop Questions

# 26. Print numbers from 1 to 10 using while loop.

# i=0
# while i<11:
#     print(i)
#     i+=1


# 27. Print even numbers from 1 to 50 using while loop.

# i = 0
# while i < 11:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 28. Print odd numbers from 1 to 50 using while loop.
# i = 0
# while i < 11:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# 29. Print the sum of first 10 natural numbers.

# sum = 0
# i = 0
# while i < 11:
#     sum += i
#     i += 1
# print(sum)

# 30. Print table of any number using while loop.

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1

# 31. Print digits of a number one by one using while loop.
#right to left 

# n = int(input("Enter a number: "))
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10

#left to right
# num = int(input("Enter the Number :"))
# print(f"Actual Number is - {num}")
# print("Digits are (left to right) :- ")
# p = len(str(num))
# while p > 0:
#     fd = num // 10**(p-1)
#     print(f"{fd}",end=" ")
#     num = num % 10**(p-1)
#     p -= 1


# 32. Count total digits of a number using while loop.

# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print("Total digits:", count)

# 33. Reverse a number using while loop.
#n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print("Reversed number:", rev)

# 34. Find sum of digits of a number.

# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10
# print("Sum of digits:", sum)

# 35. Check if a number is palindrome using while loop.


# n = int(input("Enter a number: "))
# num = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if num == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# 36. Find factorial of a number using while loop.

# n = int(input("Enter a number: "))
# fact = 1
# if n == 0:
#     fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print("Factorial:", fact)

# 37. Print Fibonacci series using while loop.

# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a, end=' ')
#     a, b = b, a + b
#     count += 1


# 38. Print numbers from 100 to 1 using while loop.

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# 39. Find the product of digits of a number.

# n = int(input("Enter a number: "))
# pro = 1
# while n > 0:
#     digit = n % 10
#     pro *= digit
#     n = n // 10
# print("Product of digits:", pro)


# 40. Display all multiples of 5 up to 100.

# i = 5
# while i <= 100:
#     print(i)
#     i += 5

# 41. Keep taking input until user enters 0.

# n = eval(input("Enter a number (0 to stop): "))
# while n != 0:
#     n = eval(input("Enter a number (0 to stop): "))        


# 42. Keep taking positive numbers and print their sum until a negative number is entered.

# sum = 0
# while True:   
#     n = int(input("Enter a positive number (negative to stop): "))
#     if n < 0:
#         break
#     sum += n
# print("Sum of positive numbers:", sum)

# 43. Input numbers until user enters "stop" (string).

# while True :
#     n = input("Enter a number (or 'stop' to end): ")
#     if n == "stop":
#         break

# 44. Find smallest digit in a number.

# n = int(input("Enter a number: "))
# s = 9
# while n > 0:
#     digit = n % 10
#     if digit < s:  
#         s = digit
#     n = n // 10   
# print("Smallest digit:", s)

# 45. Find largest digit in a number.
# n=int(input("Enter a number: "))
# m = 0
# while n > 0:
#     digit = n % 10
#     if digit > m:
#         m = digit
#     n = n // 10
# print("Largest digit:", m)    

# 46. Check if a number is Armstrong using while loop.

# n = int(input("Enter a number: "))
# num = n
# sum = 0
# p = len(str(n))
# while n > 0:
#     digit = n % 10
#     sum += digit ** p
#     n = n // 10
# if num == sum:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# 47. Count even and odd digits in a number.

# n = int(input("Enter a number: "))
# even_count = 0
# odd_count = 0
# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:    
#         even_count += 1
#     else:
#         odd_count += 1
#     n = n // 10
# print("Even digits:", even_count)
# print("Odd digits:", odd_count)



# 48. Convert decimal to binary using while loop.

# n = int(input("Enter a decimal number: "))
# binary = ""
# while n > 0:
#     binary = str(n % 2) + binary
#     n = n // 2
# print("Binary representation:", binary)

# 49. Print all factors of a number using while loop.

# n = int(input("Enter a number: "))
# i = 1
# print("Factors of", n, "are:")
# while i <= n:
#     if n % i == 0:
#         print(i,end=" ")
#     i += 1



# 50. Keep asking the password until the correct password is entered.

# password = "secret"
# while True:
#     user_input = input("Enter the password: ")
#     if user_input == password:
#         print("Access granted.")
#         break
#     else:
#         print("Incorrect password. Try again.")

