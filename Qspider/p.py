l=eval(input("Enter the list:"))
if type(i)==list:
    max=l[0]
    for i in l:
        if max>i:
            max=i
print(max)