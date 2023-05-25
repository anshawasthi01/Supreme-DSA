import heapq

# Min-Heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 6)
heapq.heappush(heap, 9)
heapq.heappush(heap, 4)
heapq.heappush(heap, 8)

print("Top element:", heap[0])
heapq.heappop(heap)
print("Size:", len(heap))
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)

if not heap:
    print("Min heap is empty")
else:
    print("Min heap is not empty")
