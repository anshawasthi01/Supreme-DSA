arr = [5,4,3,2,1]
n = len(arr)
# Bubble Sort

for i in range(1, n):
    swapCount = 0
    for j in range(n-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapCount += 1

    if swapCount == 0:
        # sort ho chuka hai, no need to check in further rounds
        break


# printing 
for i in range(n):
    print(arr[i], end=" ")


