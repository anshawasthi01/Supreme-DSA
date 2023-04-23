class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    curr = head
    next = curr.next
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def check_palindrome(head):
    if head is None:
        print("LL is empty")
        return True
    if head.next is None:
        # only 1 node
        return True

    # > 1 node in LL

    # Step A: find the middle node
    slow = head
    fast = head.next
    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next
    # slow pointer is pointing to the middle node

    # Step B: reverse LL after middle/slow node
    reverse_LL_head = reverse(slow.next)
    # join the reversed LL into the left part
    slow.next = reverse_LL_head

    # Step C: start comparison
    temp1 = head
    temp2 = reverse_LL_head
    while temp2 is not None:
        if temp1.data != temp2.data:
            # not a palindrome
            return False
        else:
            # if data is equal, then move to next node
            temp1 = temp1.next
            temp2 = temp2.next
    return True


# Test the function
head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(30)
fifth = Node(50)
sixth = Node(10)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

is_palindrome = check_palindrome(head)

if is_palindrome:
    print("LL is a valid palindrome")
else:
    print("LL is not a palindrome")
