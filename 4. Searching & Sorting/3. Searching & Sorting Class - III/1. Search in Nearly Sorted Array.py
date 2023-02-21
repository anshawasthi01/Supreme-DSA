def binarySearch(arr, target):
    s, e = 0, len(arr)-1
    mid = s + (e - s)//2

    while s <= e:
        if arr[mid] == target:
            return mid
        if mid-1 <= s and arr[mid-1] == target:
            return mid-1
        if mid+1 <= e and arr[mid+1] == target:
            return mid+1

        if target > arr[mid]:
            # right search
            s = mid + 2
        
        else:
            # left search
            e = mid - 2
        mid = s + (e - s)//2
    return -1

arr = [10, 3, 40, 20, 50, 80, 70]
target = 20

ans = binarySearch(arr, target)
print("Index of target", target, "is", ans)

        