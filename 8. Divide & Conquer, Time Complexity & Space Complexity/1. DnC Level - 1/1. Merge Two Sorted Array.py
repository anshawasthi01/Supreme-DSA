# Merge Sort Merge Function

def merge(arr, s, e):

    mid = (s + e) // 2
    len1 = mid - s + 1
    len2 = e - mid

    # assume to create arrays for len1, len2 length
    left = [0] * len1
    right = [0] * len2

    # copy values
    k = s
    i = 0
    while i < len1:
        left[i] = arr[k]
        i += 1
        k += 1

    k = mid + 1
    for i in range(len2):
        right[i] = arr[k]
        k += 1

    # merge logic
    leftIndex = 0
    rightIndex = 0
    mainArrayIndex = s

    while(leftIndex < len1 and rightIndex < len2):
        if left[leftIndex] < right[rightIndex]:
            arr[mainArrayIndex] = left[leftIndex]
            mainArrayIndex += 1
            leftIndex += 1
        else:
            arr[mainArrayIndex] = right[rightIndex]
            mainArrayIndex += 1
            rightIndex += 1

    # copy logic for left array
    while(leftIndex < len1):
        arr[mainArrayIndex] = left[leftIndex]
        mainArrayIndex += 1
        leftIndex += 1

    # copy logic for right array
    while(rightIndex < len2):
        arr[mainArrayIndex] = right[rightIndex]
        mainArrayIndex += 1
        rightIndex += 1

    # TODO : left and right wala newly created array



def mergeSort(arr, s, e):
    # base case / s == e -> single element / s > e -> invalid array
    if s >= e:
        return

    mid = (s + e) // 2
    # left part solve kardo recursion se 
    mergeSort(arr, s, mid)

    # rightpart sort krdo recursion
    mergeSort(arr, mid + 1, e)

    # now merge 2 sorted array
    merge(arr, s, e)


arr = [4, 13, 5, 13, 2, 12, 2, 2, 2, 2, 2, 2]
n = 12

s = 0
e = n - 1
# calling merge sort function
mergeSort(arr, s, e)

# printing the array
for i in range(n):
    print(arr[i], " ", end =' ')
