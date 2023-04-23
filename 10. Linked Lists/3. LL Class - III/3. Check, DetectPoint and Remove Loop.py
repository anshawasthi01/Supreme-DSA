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


def checkForLoop(head):
    if head is None:
        print("LL is empty")
        return False

    slow = head
    fast = head

    while fast != None:
        fast = fast.next
        if fast != None:
            fast = fast.next
            slow = slow.next

        if slow == fast:
            # loop present
            return True

    # fast None hogya
    return False


def startingPointLoop(head):
    if not head:
        print("LL is empty")
        return None

    slow = head
    fast = head

    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

        if slow == fast:
            slow = head
            break

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def removeLoop(head):
    if not head:
        print("LL is empty")
        return None

    slow = head
    fast = head

    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next

        if slow == fast:
            slow = head
            break

    prev = fast
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next
    prev.next = None  # 1 case m fatega have to findout
    return slow



head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(3)))))))
head.next.next.next.next.next.next = head.next.next.next
# printList(head)
print("Loop is Present or not: ", checkForLoop(head))
startPointLoop = startingPointLoop(head)
print("Starting Point of LOOP is: ", startPointLoop.data)
removeLoop(head)
printList(head)
print("Loop is Present or not: ", checkForLoop(head))