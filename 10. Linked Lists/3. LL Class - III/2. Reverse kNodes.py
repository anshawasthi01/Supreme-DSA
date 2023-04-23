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

def getLength(head):
    len = 0
    temp = head
    while temp:
        temp = temp.next
        len += 1
    return len

def reverseKNodes(head, k):
    if not head:
        print("LL is empty")
        return None
    len = getLength(head)
    if k > len:
        # print("Enter valid value for k ")
        return head

    # it means number of nodes in LL is >= k
    # Step A: reverse first k nodes of LL
    prev = None
    curr = head
    forward = curr.next
    count = 0

    while count < k:
        forward = curr.next
        curr.next = prev
        prev = curr
        curr = forward
        count += 1

    # Step B: recursive call
    if forward:
        # we still have nodes left to reverse
        recursionKaAns = reverseKNodes(forward, k)
        head.next = recursionKaAns

    # Step C: return head of the modified LL
    return prev


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
printList(head)
head = reverseKNodes(head, 3)
printList(head)