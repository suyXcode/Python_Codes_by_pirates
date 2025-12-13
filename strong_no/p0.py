#Wap to check the no. is a strong no. or not.
n=int(input("Enter The int num:"))
sum=0
a=n
while n>0:
    ld=n%10
    fact=1
    while ld>0:
        fact*=ld
        ld-=1
    sum+=fact
    n//=10
if sum==a:
    print(a,"is a strong number")
else:
    print(a,"is not a strong number")
