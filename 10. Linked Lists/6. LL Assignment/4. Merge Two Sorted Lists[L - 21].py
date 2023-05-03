# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if left == 0: return right
        if right == 0: return left

        ans = ListNode(-1)
        mptr = ans

        while left and right:
            if left.val <= right.val:
                mptr.next = left
                mptr = left
                left = left.next
            else:
                mptr.next = right
                mptr = right
                right = right.next

        if left:
            mptr.next = left
            # mptr = left
            # left = left.next

        if right:
            mptr.next = right
            # mptr = right
            # right = right.next

        return ans.next

        # # iteratively
        # result = cur = ListNode(0)
        # l1=list1
        # l2=list2
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return result.next