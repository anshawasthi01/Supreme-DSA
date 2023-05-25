def heapify(arr, n, i):
    index = i
    leftIndex = 2 * i
    rightIndex = 2 * i + 1
    largest = index

    if leftIndex <= n and arr[largest] < arr[leftIndex]:
        largest = leftIndex
    if rightIndex <= n and arr[largest] < arr[rightIndex]:
        largest = rightIndex

    # left ya right child me se koi > hogya currentNode se
    if index != largest:
        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest
        heapify(arr, n, index)


def buildHeap(arr, n):
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)


def heapSort(arr, n):
    while n != 1:
        arr[1], arr[n] = arr[n], arr[1]
        n -= 1
        heapify(arr, n, 1)


arr = [-1, 12, 56, 43, 6, 78, 87, 5, 44, 3, 23, 32]
n = 11
buildHeap(arr, n)

print("Printing the heap:")
for i in range(n + 1):
    print(arr[i], end=" ")
print()
print()

heapSort(arr, n)

print("Printing the sorted heap:")
for i in range(1, n + 1):
    print(arr[i], end=" ")
print()
