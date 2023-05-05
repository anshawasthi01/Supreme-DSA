# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/

# CodeHelp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans = [-1, -1]  # minDist, maxDist
        prev = head
        if not prev:
            return ans
        curr = head.next
        if not curr:
            return ans
        nxt = head.next.next
        if not nxt:
            return ans

        firstCP = -1
        lastCP = -1
        minDist = float('inf')
        i = 1
        while nxt:
            isCP = ((curr.val > prev.val and curr.val > nxt.val) or 
                    (curr.val < prev.val and curr.val < nxt.val))
            if isCP and firstCP == -1:
                firstCP = i
                lastCP = i
            elif isCP:
                minDist = min(minDist, i - lastCP)
                lastCP = i
            i += 1
            prev = prev.next
            curr = curr.next
            nxt = nxt.next
        if lastCP == firstCP:
            # Only 1 CP was found.
            return ans
        else:
            ans[0] = minDist
            ans[1] = lastCP - firstCP
        return ans