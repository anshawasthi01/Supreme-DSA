# https://github.com/anshawasthi01/Supreme-DSA/blob/main/4.%20Searching%20%26%20Sorting/5.%20Sorting%20Techniques/SortingCodes/main%20(5).cpp

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [5,12,4,6,1]
insertion_sort(arr)

n = len(arr)

for i in range(1, n):           # insertion sort
    val = arr[i]                # Step A - fetch
    j = i - 1                  # StepB: Compare
    for j in range(i-1, -2, -1):
        if j < 0 : break
        if arr[j] > val:
            arr[j+1] = arr[j]   # Step C: shift
        else:
            break                # rukna hai
    arr[j+1] = val               # stepD: Copy

for i in range(n):
    print(arr[i], end=" ")       # printing 

    


