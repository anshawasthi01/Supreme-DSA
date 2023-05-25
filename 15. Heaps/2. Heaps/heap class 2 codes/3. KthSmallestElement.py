import heapq

def getKthSmallestElement(arr, n, k):
    # Create a max heap
    heap = []

    # Insert initial k elements of the array
    for i in range(k):
        heapq.heappush(heap, -arr[i])

    # For remaining elements, push only if they are smaller than the top
    for i in range(k, n):
        element = arr[i]
        if element < -heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -element)

    ans = -heap[0]
    return ans

arr = [10, 5, 20, 4, 15]
n = 5
k = 2
ans = getKthSmallestElement(arr, n, k)
print("Ans is:", ans)
