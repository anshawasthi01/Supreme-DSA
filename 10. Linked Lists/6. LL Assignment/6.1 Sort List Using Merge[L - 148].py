# Code Help

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        if not left:
            return right
        if not right:
            return left

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

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Break LL into two halves using mid node.
        mid = self.findMid(head)
        left, right = head, mid.next
        mid.next = None

        # sort RE
        left = self.sortList(left)
        right = self.sortList(right)

        # merge both left ans right LLs
        mergedLL = self.merge(left, right)
        return mergedLL




















# class Solution:
#     def divide(self,head):
#         slow,fast=head,head.next
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#         return slow
    
#     def Merge(self,l,r):
#         temp=ans=ListNode()
#         while l and r:
#             if l.val<=r.val:
#                 temp.next=l
#                 l=l.next
#             else:
#                 temp.next=r
#                 r=r.next
#             temp=temp.next
#         if l:
#             temp.next=l
#         if r:
#             temp.next=r
#         return ans.next
            
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         left=head
#         right=self.divide(head)
#         temp=right.next
#         right.next=None
#         right=temp
#         left=self.sortList(left)
#         right=self.sortList(right)
#         return self.Merge(left,right)