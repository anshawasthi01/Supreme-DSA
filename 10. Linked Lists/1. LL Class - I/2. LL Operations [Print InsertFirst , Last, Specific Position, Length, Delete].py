class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # def __str__(self):
    #     return f"node {self.data} -> {self.next}"

    # def _del_(self):
        # print("Node with value:", self.data, "deleted")

def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def insertAtHead(head, data):
    if not head:
        newNode = Node(data)
        head = newNode
    else:
        newNode = Node(data)
        newNode.next = head
        head = newNode
    return head

def insertAtTail(head, data):
    if not head:
        newNode = Node(data)
        head = newNode
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head

def findLength(head):
    len = 0
    while head:
        head = head.next
        len += 1
    return len

def insertAtPosition(head, data, position):
    if not head:
        newNode = Node(data)
        head = newNode
        return head

    if position == 0:
        head = insertAtHead(head, data)
        return head

    len = findLength(head)
    if position >= len:
        head = insertAtTail(head, data)
        return head

    i = 1
    prev = head
    while i < position:
        prev = prev.next
        i += 1
    curr = prev.next
    newNode = Node(data)
    newNode.next = curr
    prev.next = newNode
    return head

def deleteNode(head, position):
    if not head:
        print("Cannot delete, linked list is empty")
        return

    if position == 1:
        temp = head
        head = head.next
        temp.next = None
        return head

    len = findLength(head)

    if position == len:
        i = 1
        prev = head
        while i < position - 1:
            prev = prev.next
            i += 1

        prev.next = None
        return head

    i = 1
    prev = head
    while i < position - 1:
        prev = prev.next
        i += 1

    curr = prev.next
    prev.next = curr.next
    curr.next = None
    return head


head = Node(1, Node(2, Node(3, Node(4))))
# head = insertAtHead(head, 4)
# head = insertAtTail(head, 10)
# listLength = findLength(head)
# head = insertAtPosition(head, 5, 3)
head = deleteNode(head, 3)
printList(head)






