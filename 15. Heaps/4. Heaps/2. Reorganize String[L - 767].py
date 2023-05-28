# https://leetcode.com/problems/reorganize-string/

# CodeHelp

import heapq
class Node:
    def __init__(self, d, c):
        self.data = d
        self.count = c

class Solution(object):
    def reorganizeString(self, s):
        # create mapping
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        maxHeap = []
        for i in range(26):
            if freq[i] != 0:
                temp = Node(chr(i + ord('a')), freq[i])
                heapq.heappush(maxHeap, (-temp.count, temp))

        ans = ""
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)[1]
            second = heapq.heappop(maxHeap)[1]

            ans += first.data
            ans += second.data

            first.count -= 1
            second.count -= 1

            if first.count != 0:
                heapq.heappush(maxHeap, (-first.count, first))

            if second.count != 0:
                heapq.heappush(maxHeap, (-second.count, second))

        if len(maxHeap) == 1:
            temp = maxHeap[0][1]
            if temp.count == 1:
                ans += temp.data
            else:
                return ""

        return ans





        # # Method 1 : Priority Queue
        # # Method 2 : Greedy ->


        # hashh = [0] * 26
        # for i in range(len(s)):
        #     hashh[ord(s[i]) - ord('a')] += 1

        # # find the most frequent char
        # max_freq_char = 0
        # max_freq = -999999999
        # for i in range(26):
        #     if hashh[i] > max_freq:
        #         max_freq = hashh[i]
        #         max_freq_char = i + ord('a')

        # index = 0
        # s = list(s)
        # while max_freq > 0 and index < len(s):
        #     s[index] = max_freq_char
        #     max_freq -= 1
        #     index += 2

        # if max_freq != 0:
        #     return ""

        # hashh[max_freq_char - ord('a')] = 0

        # # let's place the rest of the characters
        # for i in range(26):
        #     while hashh[i] > 0:
        #         index = 1 if index >= len(s) else index
        #         s[index] = i + ord('a')
        #         hashh[i] -= 1
        #         index += 2
        # return "".join(s)

