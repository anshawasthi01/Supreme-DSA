def partition(arr, s, e):
    # Step 1: Choose pivot element
    pivot_index = s
    pivot_element = arr[s]

    # Step 2: Find right position for pivot element and place it there
    count = 0
    for i in range(s + 1, e + 1):
        if arr[i] <= pivot_element:
            count += 1
   # jab main loop se bahar hua, toh mere pas pivot ki right position ka index ready h
    right_index = s + count
    arr[pivot_index], arr[right_index] = arr[right_index], arr[pivot_index]
    pivot_index = right_index

    # Step 3: Divide elements into left (smaller than pivot) and right (greater than pivot)
    # step3: left me chote and right me bade
    i, j = s, e
    while i < pivot_index and j > pivot_index:
        while arr[i] <= pivot_element and i <= e:
            i += 1
        while arr[j] > pivot_element:
            j -= 1
    # 2 case ho skte hain: A-> you found the elements to swap, B-> no need to swap
        if i < pivot_index and j > pivot_index:
            arr[i], arr[j] = arr[j], arr[i]

    return pivot_index


def quick_sort(arr, s, e):
    # Base case
    if s >= e:
        return

    # Partition the array and get the pivot index
    # partition logic, return pivotIndex
    p = partition(arr, s, e)

    # Recursively sort the left and right subarrays
    # recursive calls
    # pivot element -> left
    quick_sort(arr, s, p - 1)
    # pivot element -> right
    quick_sort(arr, p + 1, e)


# Test the implementation
arr = [0, 1, 3, 4, 5, 5, 5, 6, 9, 4, 5, 2, 2, 10, 10, 55, 10]
n = len(arr)
s, e = 0, n - 1

quick_sort(arr, s, e)

for i in range(n):
    print(arr[i], end=' ')