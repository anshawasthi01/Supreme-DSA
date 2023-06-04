# https://leetcode.com/problems/next-greater-node-in-linked-list/description/


# CodeHelp Stack
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ll = []
        while head:
            ll.append(head.val)
            head = head.next

        st = []
        # ans = [0] * len(ll)

        for i in range(len(ll)):
            while st and ll[i] > ll[st[-1]]:
                # means, ith element is the next greater of the ele idx present in stack
                kids = st[-1]
                st.pop()
                ll[kids] = ll[i]

            st.append(i)
        
        while st:
            ll[st.pop()] = 0

        return ll




