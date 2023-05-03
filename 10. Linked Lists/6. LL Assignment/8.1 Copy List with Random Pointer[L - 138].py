"""
Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# With Map
class Solution:
    def helper(self, head, mp):
        if not head:
            return None
        
        newHead = Node(head.val)
        mp[head] = newHead
        newHead.next = self.helper(head.next, mp)
        if head.random:
            newHead.random = mp[head.random]
        
        return newHead
    def copyRandomList(self, head: 'Node') -> 'Node':
        mp = {} # old node -> new node
        return self.helper(head, mp)

# # Without Map
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:
#             return None

#         # Step 1: Clone A -> A'
#         it = head  # iterate over old head
#         while it:
#             clonedNode = Node(it.val)
#             clonedNode.next = it.next
#             it.next = clonedNode
#             it = it.next.next

#         # Step 2: Assign random links of A' with the helper of A.
#         it = head
#         while it:
#             clonedNode = it.next
#             clonedNode.random = it.random.next if it.random else None
#             it = it.next.next

#         # Step 3: Detach A' from A.
#         it = head
#         clonedHead = it.next
#         while it:
#             clonedNode = it.next
#             it.next = it.next.next
#             clonedNode.next = clonedNode.next.next if clonedNode.next else None
#             it = it.next
#         return clonedHead


## class Solution:
##     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
##        hm, zero = dict(), Node(0)
        
##       cur, copy = head, zero
##      while cur:
##         copy.next = Node(cur.val)
##        hm[cur] = copy.next
##       cur, copy = cur.next, copy.next
           
## cur, copy = head, zero.next
## while cur:
##   copy.random = hm[cur.random] if cur.random else None
##  cur, copy = cur.next, copy.next
             #   
##    return zero.next