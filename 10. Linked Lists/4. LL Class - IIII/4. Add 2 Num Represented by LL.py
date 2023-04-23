class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def printList(head):
    temp = head
    while temp != None:
        print(temp.data, end=' ')
        temp = temp.next
    print()

def reverseList(head):
    prev = None
    curr = head
    while curr != None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

def addLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    # Step 1: reverse both linked lists
    head1 = reverseList(head1)
    head2 = reverseList(head2)

    # Step 2: add both linked lists
    ansHead = None
    ansTail = None
    carry = 0

    while head1 != None and head2 != None:
        # Calculate sum
        sum = carry + head1.data + head2.data
        # Find digit to create node for
        digit = sum % 10
        # Calculate carry
        carry = sum // 10

        # Create a new Node for the digit
        newNode = Node(digit)
        # Attach the newNode into the answer linked list
        if ansHead == None:
            # First node insert krre ho
            ansHead = newNode
            ansTail = newNode
        else:
            ansTail.next = newNode
            ansTail = newNode

        head1 = head1.next
        head2 = head2.next

    # Jab head1 list ki length head2 list se jada hogi
    while head1 != None:
        sum = carry + head1.data
        digit = sum % 10
        carry = sum // 10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode
        head1 = head1.next

    # Jab head2 list ki length head1 list se jada hogi
    while head2 != None:
        sum = carry + head2.data
        digit = sum % 10
        carry = sum // 10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode
        head2 = head2.next

    # Handle carry ko alag se
    while carry != 0:
        sum = carry
        digit = sum % 10
        carry = sum // 10
        newNode = Node(digit)
        ansTail.next = newNode
        ansTail = newNode

    # Step 3: reverse the ans linked list
    ansHead = reverseList(ansHead)
    return ansHead

head1 = Node(9)
second1 = Node(9)
head1.next = second1

head2 = Node(9)
second2 = Node(9)
third2 = Node(4)
head2.next = second2
second2.next = third2

ans = addLists(head1, head2)

printList(ans)
