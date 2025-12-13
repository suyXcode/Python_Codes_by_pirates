n = int(input("Enter number of terms: "))

fib = (0, 1)
for _ in range(n):
    print(fib[0], end=" ")
    fib = (fib[1], fib[0] + fib[1])
