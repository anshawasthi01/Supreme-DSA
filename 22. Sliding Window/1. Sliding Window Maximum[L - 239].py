# https://leetcode.com/problems/sliding-window-maximum/description/

# CodeHelp
# Sliding Window
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        # we will store indexes in deque
        ans = []

        # Process first k size window
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # insert element
            dq.append(i)

        # ans store karlo for 1st window
        ans.append(nums[dq[0]])

        # Remaining windows
        for i in range(k, len(nums)):
            # Removal
            if dq and i - k >= dq[0]:
                dq.popleft()

            # Additional
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # insert element
            dq.append(i)

            # ans store
            ans.append(nums[dq[0]])

        return ans


# QUEUE
# from collections import deque
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         dq = deque()
#         ans = []

#         # first window of k size
#         for i in range(k):
#             # chote element remove krdo, 
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()
#             # inserting index, so tht we can checkout of window element
#             dq.append(i)

#         # store answer for first window
#         ans.append(nums[dq[0]])

#         # remaining windows ko process
#         for i in range(k, len(nums)):
#             # out of window element ko remove krdia 
#             if dq and i - dq[0] >= k:
#                 dq.popleft()

#             # ab ferse current element k liyue chotte element 
#             # ko remove krna h 
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()
#             # inserting index, so tht we can checkout of window element
#             dq.append(i)

#             # current window ka answer store krna h 
#             ans.append(nums[dq[0]])

#         return ans
