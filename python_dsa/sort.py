l = eval(input("Enter the list :"))

if type(l) == list:
    l.sort()
    # n = len(l)

    # for i in range(n-1):
    #     min_index = i
    #     for j in range(i+1,n):
    #         if l[j] < l[min_index]:
    #             min_index = j
    #     min_value = l.pop(min_index)
    #     l.insert(i,min_value)
    print("Sorted List:",l)

else:
    print("Given data is not list.")