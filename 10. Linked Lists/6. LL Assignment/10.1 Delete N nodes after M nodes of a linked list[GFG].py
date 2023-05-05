# https://practice.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# CodeHelp
'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        if not head:
            return
        it = head
        for i in range(M - 1):
            # if M nodes are N.A.
            if not it:
                return
            it = it.next

        # it -> would be at Mth node
        if not it:
            return

        MthNode = it
        it = MthNode.next
        for i in range(N):
            if not it:
                break
            temp = it.next
            del it
            it = temp

        MthNode.next = it
        self.skipMdeleteN(it, M, N)
