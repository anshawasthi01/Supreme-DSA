# https://leetcode.com/problems/longest-happy-string/


# CodeHelp Python noy Python3

import heapq
class Node:
    def __init__(self, d, c):
        self.data = d
        self.count = c
    
    def __lt__(self, other):
        return self.count < other.count

class Solution(object):
    def longestDiverseString(self, a, b, c):
        maxHeap = []
        if a > 0:
            temp = Node('a', a)
            heapq.heappush(maxHeap, (-temp.count, temp))
        
        if b > 0:
            temp = Node('b', b)
            heapq.heappush(maxHeap, (-temp.count, temp))
        
        if c > 0:
            temp = Node('c', c)
            heapq.heappush(maxHeap, (-temp.count, temp))

        ans = ""
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)[1]
            second = heapq.heappop(maxHeap)[1]

            if first.count >= 2:
                ans += first.data
                ans += first.data
                first.count -= 2
            else:
                ans += first.data
                first.count -= 1

            if second.count >= 2 and second.count >= first.count:
                ans += second.data
                ans += second.data
                second.count -= 2
            else:
                ans += second.data
                second.count -= 1

            if first.count > 0:
                heapq.heappush(maxHeap, (-first.count, first))

            if second.count > 0:
                heapq.heappush(maxHeap, (-second.count, second))

        if len(maxHeap) == 1:
            temp = maxHeap[0][1]
            if temp.count >= 2:
                ans += temp.data
                ans += temp.data
                temp.count -= 2
            else:
                ans += temp.data
                temp.count -= 1

        return ans