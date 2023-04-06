# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

# def countInversions(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count


def merge(arr, temp, start, mid, end):
    i, j, k = start, mid + 1, start
    count = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:    
            temp[k] = arr[i]
            k += 1
            i += 1
        else:           # arr[i] > arr[j] Inversion Count Case
            temp[k] = arr[j]
            k += 1
            j += 1
            count += mid - i + 1
            
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
        
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1
        
    while start <= end:
        arr[start] = temp[start]
        start += 1
    return count
            
def mergeSort(arr, temp, start, end ):
    if start >= end: return 0
    mid = start + (end - start) // 2
    count = 0
    count += mergeSort(arr, temp, start, mid)
    count += mergeSort(arr, temp, mid + 1, end)
    count += merge(arr, temp, start, mid, end)
    return count
    
def countInversions(arr):
    count = 0
    temp = [0] * len(arr)
    count = mergeSort(arr, temp, 0, len(arr) - 1 )
    return count
    