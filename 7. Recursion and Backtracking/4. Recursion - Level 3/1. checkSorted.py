def checkSorted(arr, n, i):
    # base case
    if(i == n-1):
        return True

    # 1 case solve krna h
    if(arr[i+1] <= arr[i]):
        return False

    # baaki recursio sambhal lega
    ans = checkSorted(arr, n, i+1)
    return ans

arr = [4,3,1,2,4,4]
n = len(arr)
i = 0
isSorted = checkSorted(arr, n, i)

if(isSorted):
    print("Array is sorted")
else:
    print("Array is not sorted")
