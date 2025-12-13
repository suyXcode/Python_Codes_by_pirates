#Factorial of given number

n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact}.")