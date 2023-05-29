# Python does not have switch

import heapq
def signum(a, b):
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

def callMedian(median, maxHeap, minHeap, element):

    if signum(len(minHeap), len(maxHeap)) == 0:
        if element > median[0]:
            heapq.heappush(minHeap, element)
            median[0] = minHeap[0]
        else:
            heapq.heappush(maxHeap, -element)
            median[0] = -maxHeap[0]

    elif signum(len(minHeap), len(maxHeap)) == 1:
        if element > median[0]:
            minTop = heapq.heappushpop(minHeap, element)
            heapq.heappush(maxHeap, -minTop)
            median[0] = (minHeap[0] - maxHeap[0]) / 2.0
        else:
            heapq.heappush(maxHeap, -element)
            median[0] = (minHeap[0] - maxHeap[0]) / 2.0
            
    elif signum(len(minHeap), len(maxHeap)) == -1:
        if element > median[0]:
            heapq.heappush(minHeap, element)
            median[0] = (minHeap[0] - maxHeap[0]) / 2.0
        else:
            maxTop = -heapq.heappushpop(maxHeap, -element)
            heapq.heappush(minHeap, maxTop)
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
