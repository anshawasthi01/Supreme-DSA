# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

# CodeHelp

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-x for x in piles]
        heapq.heapify(maxHeap)

        while k > 0:
            maxElement = -heapq.heappop(maxHeap)
            maxElement = maxElement - math.floor(maxElement / 2)
            heapq.heappush(maxHeap, -maxElement)
            k -= 1

        return -sum(maxHeap)


        # arr=[]
        # for n in piles:
        #     heapq.heappush(arr,-1*n)
        # while k>0:
        #     x=heapq.heappop(arr)
        #     heapq.heappush(arr,x//2)
        #     k-=1
        # return sum(arr)*-1