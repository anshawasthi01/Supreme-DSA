n = int(input("Enter the size of array "))

def findUnique(arr):
    ans = 0
    for i in range(len(arr)):
        ans = ans ^ arr[i]
    return ans


arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele) 

uniqueElement = findUnique(arr);
print("Unique Element is ", uniqueElement)