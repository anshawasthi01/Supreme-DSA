# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

# CodeHelp
import heapq
class Node:
    def __init__(self, data: int, row: int, col: int):
        self.data = data
        self.row = row
        self.col = col
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mini = float('inf')
        maxi = float('-inf')

        minHeap = []
        k = len(nums)
        for i in range(k):
            element = nums[i][0]
            maxi = max(maxi, element)
            mini = min(mini, element)
            heapq.heappush(minHeap, Node(element, i, 0))

        ansStart = mini
        ansEnd = maxi

        while minHeap:
            top = heapq.heappop(minHeap)
            topelement = top.data
            topRow = top.row
            topCol = top.col

            # mini updated
            mini = topelement

            currRange = maxi - mini
            ansRange = ansEnd - ansStart
            if currRange < ansRange:
                ansStart = mini
                ansEnd = maxi

            # check for new element in the same list
            if topCol + 1 < len(nums[topRow]):
                maxi = max(maxi, nums[topRow][topCol + 1])
                newNode = Node(nums[topRow][topCol + 1], topRow, topCol + 1)
                heapq.heappush(minHeap, newNode)
            else:
                break

        return [ansStart, ansEnd]






