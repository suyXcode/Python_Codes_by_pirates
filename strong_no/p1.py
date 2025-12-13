#Wap to check the no. is a strong no. or not using for loop
n=int(input("Enter the No : "))
a=n
sum=0
for i in str(n):
    ld=int(i)
    fact=1
    for j in range(1,ld+1):
        fact*=j
    sum+=fact
if sum==a:
    print(a,"is a strong number")
else:
    print(a,"is not a strong number")
