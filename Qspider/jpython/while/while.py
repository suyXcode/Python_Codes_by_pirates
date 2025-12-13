# # Looping statement :-

# # ====================

# # 1.Wap to print n natural numbers

# # n=int(input("Enter The int num:"))
# # i=1
# # while i<=n:
# #     print(i)
# #     i+=1


# # 2.Wap to print n natural numbers in reverse order.

# # 3.Wap to print natural numbers in a given range

# # 4.Wap to print user name 10 times

# # 5.Wap to print the multiplication table.

# # 6.Wap to print n natural even numbers.

# # 7.Wap to print n natural odd numbers.

# # n = int(input("Enter how many odd numbers you want: "))
# # i = 1
# # count = 0
# # while count < n:   
# #     if i % 2 != 0:  
# #         print(i)
# #         count += 1  
# #     i += 1




# # 8.Wap to print n natural palindrome numbers

# # 9.Wap to print the sum of n natural number

# # 10.Wap to print product of n natural numbers.

# # 11.Wap to print factorial a number.

# # 12.Wap to print the digits of a number

# # 13.Wap to find the sum of digits of a number.

# # 14.Wap to find the product of digits of a number.

# # 15.Wap to reverse a number without using slicing

# # 16.Wap to reverse a number without using type casting and slicing.

# # 17.Wap to count the no. of zeros present in a number

# # 18.Wap to print the factors of a number.

# # 19.Wap check the no. is prime or not

# # 20.Wap to check the no. is Armstrong no. or not. #153,370

# # 21.Wap to check the no. disarium no. or not. #89,135,175

# # 22.Wap to check the given number is a Harshad no. or not #36,18,132

# # 23.Check the given no.is spy number or not. #1124,123,22

# # 24.Wap to check the no. is perfect no. or not

# # 25.Wap to check the no. is a strong no. or not.

# #-------------------------------------------
# # 26.Wap to check is xylem or phloem no.
# #-------------------------------------------

# # 27.Create a list of n no. values provided by the user

# # 28.Given a list of numbers, count how many are even and how many are odd.




# #----------------------------------------------------------------------------------
# # 29.Wap to print all the values of a collection (str, list, tuple)

# # 30.Wap to print the string values from a given a list

# # 31.Wap to extract all the palindrome word from a given list

# #   s1 = [10,404,'hii',4.5,'eye',7-8j,'bye','madam',202]

# #   o/p= ['eye', 'madam']

# # 32.Wap to print all the characters of a string

# # 33.Wap to print all vowels present in a word

# # 34.Wap to extract all the strings from a list.

# # 35.Wap to extract all the palindrome no. from a list

# # 36.Wap to return a tuple containing n natural odd numbers

# # 37.Wap to print all the values of a set

# # 38.Wap to extract all the float values from a set and store in a list

# # 39.Wap to toggle the string

# # 40.Wap to reverse the given word


# # Nested loop :-

# # ============

# # Wap to extract all the prime numbers from a given list
# # Wap to extract all the Armstrong number from a given list.
# # Wap to extract all the perfect numbers from a tuple
# # Wap to extract the xylem numbers from a list


# n=int(input("Enter :"))
# sum=0
# pro=1
# while n>0:
#     ld=n%10
#     if ld%2==0:
#         sum+=ld
#     else:
#         pro*=ld
#     n//=10
# print("Sum:",sum)
# print("Product:",pro)



n=int(input("Enter :"))
for i in range(n,0,-1):
    print(i)