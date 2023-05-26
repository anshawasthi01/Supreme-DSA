# Code Help Python not Python3

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        minHeap = []

        k = len(lists)
        if k == 0:
            return None

        # first element of every linked list ko insert kardo heap me
        for i in range(k):
            if lists[i] != None:
                heapq.heappush(minHeap, (lists[i].val, lists[i]))  # Highlighted change

        head = tail = None

        while minHeap:
            temp = heapq.heappop(minHeap)[1] 
            # temp may or may not be the first element of the answer linked list
            if head == None:
                # temp is the first element of the answer linked list
                head = tail = temp
                if tail.next != None:
                    heapq.heappush(minHeap, (tail.next.val, tail.next))

            else:
                # temp is not the first element of the linked list
                tail.next = temp
                tail = temp
                if tail.next != None:
                    heapq.heappush(minHeap, (tail.next.val, tail.next))

        return head

        # Devsnest
        # hp= []
        # for head in lists:
        #     if head:
        #         heapq.heappush(hp, (head.val, head))
        # ans = ListNode()
        # p = ans
        # while hp:
        #     el = heapq.heappop(hp)[1]
        #     p.next = el
        #     p = p.next
        #     if el.next:
        #         heapq.heappush(hp, (el.next.val, el.next))
        # return ans.next
        