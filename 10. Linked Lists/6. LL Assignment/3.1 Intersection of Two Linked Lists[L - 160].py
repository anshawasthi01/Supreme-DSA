# https://leetcode.com/problems/intersection-of-two-linked-lists/description/


# CodeHelp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next

        if not a and not b:
            return None

        if not a:
            # B LL is bigger or equal.
            # we need to find out how much bigger it is.
            blen = 0
            while b:
                blen += 1
                b = b.next

            while blen > 0:
                headB = headB.next
                blen -= 1
        else:
            # A LL is bigger.
            # we need to find out how much bigger it is.
            alen = 0
            while a:
                alen += 1
                a = a.next

            while alen > 0:
                headA = headA.next
                alen -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

        