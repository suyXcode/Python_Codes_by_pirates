#---------------------
# List comprehension
#---------------------

# create a list of numbers from 1 to 10
'''
list1 = [var for var in range(1,11)]
print(list1)
'''
# list of na ntural numbers
'''
n = int(input("Enter a number : "))
print([ i for i in range(1,n+1)])
'''
# list of odd natural numbers

'''
n = int(input("Enter a number : "))
list1 = [i for i in range(1,n+1) if i%2 == 1 ]
print(list1)
'''

# list of squares of n natural even numbers
'''
n = int(input("Enter a number : "))
list1 = [ i**2 for i in range(1,n+1) if i%2 == 0]
print(list1)
'''
# list of n natural palindrome numbers
n = int(input("Enter a number : "))
list1 = [i for i in range(1,n+1) if str(i) == str(i)[::-1]]
print(list1)

# list containin the length of words of a string

s = "This is a string"
l1 = [4,2,1,6]

s = "Hello everyone"
l2 = [5,8]

