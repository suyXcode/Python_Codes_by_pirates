# wap a progrm using recursion if user input 3 then result is 32123
# def mi(n , m):
#     if n == 0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         print(n, end="")
#         return mi(n-1, m + str(n))  
    
# n = int(input("Enter a number: "))
# mi(n, "")


def mi(n,rev=0):
    # if n==0:
    #     return 0
    if n==1:
        return 1
    else:
        rev = rev*10+ n%10
        print(str(rev)+str(rev)[-2::-1])

    return mi(n-1,rev)
print(mi(3))

