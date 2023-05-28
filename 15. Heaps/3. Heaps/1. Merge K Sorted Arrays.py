import heapq

class Info:
    def __init__(self, val, r, c):
        self.data = val
        self.row = r
        self.col = c

    def __lt__(self, other):
        return self.data < other.data

def mergeKSortedArrays(arr, k, n):
    minHeap = []
    
    # Insert the first element of each array into the min heap
    # hr array ka first element insert karo
    for i in range(k):
        temp = Info(arr[i][0], i, 0)
        heapq.heappush(minHeap, temp)
    
    ans = []
    
    while minHeap:
        temp = heapq.heappop(minHeap)
        topElement = temp.data
        topRow = temp.row
        topCol = temp.col
        
        ans.append(topElement)
        
        if topCol + 1 < n:
            newInfo = Info(arr[topRow][topCol+1], topRow, topCol+1)
            heapq.heappush(minHeap, newInfo)
    
    return ans

arr = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [0, 9, 10, 11]
    ]

k = 3
n = 4

ans = mergeKSortedArrays(arr, k, n)
for i in ans:
    print(i, end=" ")
print()
