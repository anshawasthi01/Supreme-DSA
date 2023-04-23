class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def getMiddle(head):
    if not head:
        print("LL is empty")
        return head
    if not head.next:
        # only 1 node in LL
        return head

    # LL have > 1 node
    slow = head
    fast = head.next # for even ll we can choose by adding next or not according to our choice

    while slow and fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

    return slow

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
printList(head)
middle = getMiddle(head)
print(middle.data)
