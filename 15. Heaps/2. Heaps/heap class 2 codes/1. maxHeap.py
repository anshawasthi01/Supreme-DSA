import heapq

# Max-Heap
heap = [3, 6, 9, 4]
heapq.heappush(heap, 8)

print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)
print("Top element:", heap[0])
heapq.heappop(heap)

print("Size:", len(heap))
if not heap:
    print("Max heap is empty")
else:
    print("Max heap is not empty")
