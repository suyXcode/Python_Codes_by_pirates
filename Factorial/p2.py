#iterative method to find factorial of a number
# Time complexity: O(N)
# Space complexity: O(1)



num = int(input("Enter a number: "))
fact = 1

# Factorial of negative number doesn't exist

if num < 0:
    print("Not Possible")
else:
    for i in range(1, num+1):
        fact = fact * i

print("Factorial of", num, "is", fact)
