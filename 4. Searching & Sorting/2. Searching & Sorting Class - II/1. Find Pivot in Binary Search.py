def findPivot(arr):
    s, e = 0, len(arr)-1 

    while s <= e:
        mid = s + (e-s)//2

        if mid+1 < len(arr) and arr[mid] > arr[mid+1]:
            return mid

        if mid-1 >= 0 and arr[mid-1] > arr[mid]:
            return mid - 1


        if arr[s] >= arr[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return s


arr = [3,4,5,7,1,2]
ans = findPivot(arr)
print("Pivot Element is : ",arr[ans])