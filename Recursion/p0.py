n= int(input("Enter the num :"))
s=n
rev=0 
while s>0:
   rev = rev*10 + n%10
   n//=10
print("rev",rev)
