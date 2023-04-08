class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"node {self.data} -> {self.next}"

# Creation of List 
# a = Node(1)
# a.next = Node(2)
# a.next.next = Node(3)

a = Node(1, Node(2, Node(3, Node(4))))

# Print Linked List
def print_ll(head):
    while head:
        print(head.data, "-> ", end = '')
        head = head.next
    print(None)
# print_ll(b)

# Insert at front
def insert_at_front(head, data):
    x = Node(data)
    x.next = head
    return x
    # OR
    return Node(data, head)

# Insert at Last
def insert_at_last(head, data):
    if not head:
        return Node(Node)
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = Node(data)
    return head
print(insert_at_last(a,5))
