# have multiple piece of ropes

import heapq

arr = [4, 3, 2, 6]
n = 4

# minHeap
pq = []
for i in range(n):
    heapq.heappush(pq, arr[i])

cost = 0
while len(pq) != 1:
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)

    cost += first + second
    newLength = first + second
    heapq.heappush(pq, newLength)

print("Cost is:", cost)
