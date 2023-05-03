# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem


def fun(head, positionFromTail, ans):
    if head is None: 
        return
    fun(head.next, positionFromTail, ans)
    if positionFromTail[0] == 0:
        ans[0] = head.data
    positionFromTail[0] -= 1
    
def getNode(llist, positionFromTail):
    positionFromTail = [positionFromTail]
    ans = [-1]
    fun(llist, positionFromTail, ans)
    return ans[0]