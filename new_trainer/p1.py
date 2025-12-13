# 1.	Write a program to check whether a number is positive, negative, or zero.

# n = int(input(“Enter the num:”))
# if n>0:
# 	print(“+ve”)
# elif n<0:
# 	print(“-ve”)
# else:
# 	print(“zero”)

# 2. Write a program to check whether a number is even or odd.
# n = int(input(“Enter the num:”))
# if n%2==1:
# 	print(“odd num”)
# else:
# 	print(“even num”)


# 3. Check if a given character is a vowel or consonant.
# s = input(“enter the character :”)
# if s in “AEIOUaeiou”:
# 	print(“Vowel”)
# else:
# 	print("Consonant”)



# 4. Check whether a number is divisible by 5 and 11 or not.
# n = int(input(“Enter the num:”))
# if n%5==0 and n%11=0:
# 	print(“divisible”)
# else:
# 	print(“not divisible”)


# 5. Check whether a year is a leap year or not.
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# 6. Check whether the input is uppercase, lowercase, digit, or special character.

# ch = input("Enter a character: ")
# if 'A' <= ch <= 'Z':
#     print("Uppercase letter")
# elif 'a' <= ch <= 'z':
#     print("Lowercase letter")
# elif '0' <= ch <= '9':
#     print("Digit")
# else:
#     print("Special character")


# 7. Write a program to find the largest of three numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)    




# 8. Take a user's age and check if they are eligible to vote.

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")



# 9. Check if a student passed or failed (Pass if marks ≥ 33).

# marks = int(input("Enter your marks: "))
# if marks >= 33:
#     print("Passed")
# else:
#     print("Failed")


# 10. Check grade of a student using percentage:

# A: 90+

# B: 80–89

# C: 70–79

# D: 60–69

# F: Below 60

# percentage = float(input("Enter your percentage: "))
# if percentage >= 90:
#     print("Grade: A")
# elif percentage >= 80:
#     print("Grade: B")
# elif percentage >= 70:
#     print("Grade: C")
# elif percentage >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")





# 11. Check if a number is a multiple of 3 or not.

# n = int(input("Enter a number: "))
# if n % 3 == 0:
#     print("Multiple of 3")
# else:
#     print("Not a multiple of 3")



# 12. Check if the entered number is prime or not (without loop, using nested if for small numbers).

# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Not a prime number")
# elif n == 2 or n == 3:
#     print("Prime number")
# elif n % 2 == 0 or n % 3 == 0:
#     print("Not a prime number")
# else:
#     print("Prime number")


# 13. Check if a number is a single-digit or double-digit or three-digit.
# n = int(input("Enter a number: "))
# if 0 <= n <= 9:
#     print("Single-digit number")
# elif 10 <= n <= 99:
#     print("Double-digit number")
# elif 100 <= n <= 999:
#     print("Three-digit number")



# 14. Input amount and apply discount: if amount > 1000 give 10% discount else 5%.

# amount = float(input("Enter the amount: "))
# if amount > 1000:
#     discount = amount * 0.10
# else:
#     discount = amount * 0.05
# final_amount = amount - discount
# print("Final amount after discount:", final_amount)




# 15. Check if a character is alphabet or not.
# ch = input("Enter a character: ")
# if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
#     print("Alphabet")
# else:
#     print("Not an alphabet")



# 16. Check if a number ends with digit 3.
# n = int(input("Enter a number: "))
# if n % 10 == 3:
#     print("Ends with digit 3")
# else:
#     print("Does not end with digit 3")



# 17. Compare two strings and check if they are equal or not.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if str1 == str2:
#     print("Strings are equal")
# else:
#     print("Strings are not equal")



# 18. Check if the number is perfect square or not.

# num = int(input("Enter a number: "))
# sqrt = int(num**0.5)
# if sqrt * sqrt == num:
#     print("Perfect square")
# else:
#     print("Not a perfect square")


# 19. Check if temperature is Hot, Moderate, or Cold (based on values).

# temp = float(input("Enter the temperature in Celsius: "))
# if temp > 30:
#     print("Hot")
# elif 15 <= temp <= 30:
#     print("Moderate")
# else:
#     print("Cold")



# 20. Check if a given day number (1–7) is weekday or weekend.
# day = int(input("Enter day number (1-7): "))
# if day in [6, 7]:
#     print("Weekend")
# else:
#     print("Weekday")


# 21. Check if the input number is Armstrong number (for 3-digit) not using loop.

# n = int(input("Enter a 3-digit number: "))
# hundreds = n // 100
# tens = (n // 10) % 10
# units = n % 10
# if n == hundreds**3 + tens**3 + units**3:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")





# 22. Check if the number is palindrome or not (without loops).
# n = int(input("Enter a number: "))
# if n == int(str(n)[::-1]):
#     print("Palindrome")
# else:
#     print("Not a palindrome")



# 23. Validate password: at least 8 characters.

# password = input("Enter a password: ")
# if len(password) >= 8:
#     print("Valid password")
# else:
#     print("Invalid password, must be at least 8 characters long")



# 24. Check if a person is child, adult, or senior citizen.

# age = int(input("Enter your age: "))
# if age < 18:
#     print("Child")
# elif 18 <= age < 60:
#     print("Adult")
# else:
#     print("Senior Citizen")



# 25. Take two numbers and check if the first is divisible by the second or not.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num2 != 0 and num1 % num2 == 0:
#     print(f"{num1} is divisible by {num2}")
# else:
#     print(f"{num1} is not divisible by {num2}")






