class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

    def __del__(self):
        print(f"Node with value: {self.data} deleted")

def reverseusingLoop(head):
    prev = None
    curr = head

    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

def reverse(prev, curr):
    if curr == None:
        return prev

    forward = curr.next
    curr.next = prev

    return reverse(curr, forward)

def reverseusingRecursion(prev, curr):
    if curr == None:
        return prev

    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

    return reverseusingRecursion(prev, curr)

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next

# Sample usage
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Output linked list
print("Linked List:")
printList(head)
print()

# Reverse linked list using recursion
prev, curr = None, head
head = reverseusingRecursion(prev, curr)
print("\nReverse Linked List using Recursion: ")
printList(head)
print()

# Reverse linked list using loop
head = reverseusingLoop(head)
print("Reverse Linked List using Loop:")
printList(head)
print()




