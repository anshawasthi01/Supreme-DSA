# https://leetcode.com/problems/rotate-list/description/

# CodeHelp

class Solution:
    def getLength(self, head: ListNode) -> int:
        len = 0
        while head:
            len += 1
            head = head.next
        return len
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        len = self.getLength(head)
        actualRotateK = k % len
        
        if actualRotateK == 0:
            return head
        
        newLastNodePos = len - actualRotateK - 1
        newLastNode = head
        
        for i in range(newLastNodePos):
            newLastNode = newLastNode.next
        
        newHead = newLastNode.next
        newLastNode.next = None
        
        it = newHead
        while it.next:
            it = it.next
        
        it.next = head
        
        return newHead
