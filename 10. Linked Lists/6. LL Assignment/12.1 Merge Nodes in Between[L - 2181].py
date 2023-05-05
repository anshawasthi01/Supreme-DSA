# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# CodeHelp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow = head
        fast = head.next
        new_last_node = None
        sum = 0

        while fast:
            if fast.val != 0:
                sum += fast.val
            else:
                # fast.val == 0
                slow.val = sum
                new_last_node = slow
                slow = slow.next
                sum = 0

            fast = fast.next

        # just formed new list
        new_last_node.next = None

        # Deleting old List.
        # while head:
        #     nxt = head.next
        #     del head
        #     head = nxt

        return head