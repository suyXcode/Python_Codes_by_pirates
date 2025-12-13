#Factorial of n natural numbers
n=int(input("Enter a number: "))
i=0
while i<=n:
    fact=1
    for j in range(1,i+1):
        fact = fact * j
    print("Factorial of", i, "is", fact)
    i += 1