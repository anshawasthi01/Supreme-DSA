class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def remove_duplicates(head):
    if head is None:
        print("LL is empty")
        return
    if head.next is None:
        print("Single Node in LL")
        return

    # >1 node in LL
    curr = head

    while curr is not None:
        if curr.next is not None and curr.data == curr.next.data:
            #equal
            temp = curr.next
            curr.next = curr.next.next
            #delete node
            temp.next = None
            del temp
        else:
            # not equal
            curr = curr.next

# creating the linked list
head = Node(1)
second = Node(2)
third = Node(2)
fourth = Node(3)
fifth = Node(4)
sixth = Node(4)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("Input LL: ", end="")
print_list(head)

remove_duplicates(head)
print("Output LL: ", end="")
print_list(head)
