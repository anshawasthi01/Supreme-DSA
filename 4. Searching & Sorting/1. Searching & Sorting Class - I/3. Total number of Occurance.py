def firstOccurance(arr, target):
    s, e = 0, len(arr)-1
    mid = s + (e - s)//2
    ans = -1
    while s <= e:
        if arr[mid] == target:
            # ans store
            ans = mid
            # then left
            e = mid - 1
        
        elif target < arr[mid]:
            # left me search
            e = mid - 1

        elif target > arr[mid]:
            # right search
            s = mid + 1
        
        mid = s + (e - s)//2

    return ans


def lastOccurance(arr, target):
    s, e = 0, len(arr)-1
    mid = s + (e - s)//2
    ans = -1

    while s <= e:
        if arr[mid] == target:
            # ans store
            ans = mid
            # right search
            s = mid + 1
        
        elif target < arr[mid]:
            # left search
            e = mid - 1

        elif target > arr[mid]:
            # right search
            s = mid + 1
        
        mid = s + (e - s)//2
    return ans

arr = [1,2,3,3,3,3,3,3,3,9,11,12,12]
target = 3

TotalOccurance = lastOccurance(arr, target) - firstOccurance(arr, target) + 1
print("ans is : ", TotalOccurance)