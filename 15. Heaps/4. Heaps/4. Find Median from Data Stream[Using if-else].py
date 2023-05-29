import heapq
def callMedian(median, maxHeap, minHeap, element):
    if len(minHeap) == len(maxHeap):
        if element > median[0]:
            heapq.heappush(minHeap, element)
            median[0] = minHeap[0]
        else:
            heapq.heappush(maxHeap, -element)
            median[0] = -maxHeap[0]

    elif len(maxHeap) > len(minHeap):
        if element > median[0]:
            heapq.heappush(minHeap, element)
            median[0] = (minHeap[0] - maxHeap[0]) / 2

        else:
          maxTop = -maxHeap[0]
          heapq.heappop(maxHeap)
          heapq.heappush(minHeap, maxTop)
          heapq.heappush(maxHeap, -element)
          median[0] = (minHeap[0] - maxHeap[0]) / 2.0  # -Coz maxHeap Implementation

    else:
        # len(maxHeap) < len(minHeap)
        if element > median[0]:
            minTop = minHeap[0]
            heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -minTop)
            heapq.heappush(minHeap, element)
            median[0] = (minHeap[0] - maxHeap[0]) / 2.0

        else:
            heapq.heappush(maxHeap, -element)
            median[0] = (minHeap[0] - maxHeap[0]) / 2.0

arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
n = 12

median = [0]
maxHeap = []
minHeap = []

for i in range(n):
    element = arr[i]
    callMedian(median, maxHeap, minHeap, element)
    print(f"arr[i]->median: {median[0]}")
