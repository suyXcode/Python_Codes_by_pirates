'''Sometimes we want to perform actions that are not built into Python.

Then we can create our own algorithms.

For example, an algorithm can be used to find the lowest value in a list, like in the example below:

Create an algorithm to find the lowest value in a list:

'''
# arr = [7, 12, 9, 4, 11, 8]
# lowest=arr[0]
# for i in arr:
#     if i<lowest:
#         lowest=i
#     else:
#         continue                                         
# print(f"Lowest value in the list/array is: {lowest}")


'''Create an algorithm to find the maximum value in a list:'''
# arr = [7, 12, 9, 4, 11, 8]
# maxele=arr[0]
# for i in arr:
#     if i>maxele:
#         maxele=i
#     else:
#         continue
# print(f"Maximum value in the list/array is: {maxele}")
'''Create an algorithm to find the average value in a list:'''
# arr = [7, 12, 9, 4, 11, 8]
# sum=0
# count=1
# for i in arr:
#     if type(i)==int:
#         sum+=i
#         count+=1
# print(f"Average of this list/arr is : {sum/count}")

'''Create an algorithm to find the sort in a list:'''

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(mylist)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)
