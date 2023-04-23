class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def printList(head):
    temp = head
    while(temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    print()

def sortZeroOneTwo(head):
    # Step 1: Find count of zeroes, ones and twos
    zero = one = two = 0

    temp = head
    while(temp != None):
        if(temp.data == 0):
            zero += 1
        elif(temp.data == 1):
            one += 1
        elif(temp.data == 2):
            two += 1
        temp = temp.next

    # Step 2: Fill 0, 1 and 2s in the original ll
    temp = head
    # Fill zeroes
    while(zero > 0):
        temp.data = 0
        temp = temp.next
        zero -= 1
    # Fill ones
    while(one > 0):
        temp.data = 1
        temp = temp.next
        one -= 1
    # Fill 2s
    while(two > 0):
        temp.data = 2
        temp = temp.next
        two -= 1

def sort2(head):
    if(head == None):
        print("LL is empty")
        return None
    if(head.next == None):
        # Single node in LL
        return head

    # Create dummy nodes
    zeroHead = Node(-101)
    zeroTail = zeroHead

    oneHead = Node(-101)
    oneTail = oneHead

    twoHead = Node(-101)
    twoTail = twoHead

    # Traverse the original LL
    curr = head
    while(curr != None):
        if(curr.data == 0):
            # Take out the zero wali node
            temp = curr
            curr = curr.next
            temp.next = None

            # Append the zero node in zeroHead LL
            zeroTail.next = temp
            zeroTail = temp
        elif(curr.data == 1):
            # Take out the one wali node
            temp = curr
            curr = curr.next
            temp.next = None

            # Append the one node in oneHead LL
            oneTail.next = temp
            oneTail = temp
        elif(curr.data == 2):
            # Take out the two wali node
            temp = curr
            curr = curr.next
            temp.next = None

            # Append the two node in twoHead LL
            twoTail.next = temp
            twoTail = temp

    # Ab yaha par, zero, one, two, teeno LL ready hain

    # Join them
    # Remove dummy nodes

    # Modify one wali list
    temp = oneHead
    oneHead = oneHead.next
    temp.next = None
    del temp

    # Modify two wali list
    temp = twoHead
    twoHead = twoHead.next
    temp.next = None
    del temp

    # Join list
    if(oneHead != None):
        # One wali list is non-empty
        # Zero wali list ko one wali list se attach kar dia
        zeroTail.next = oneHead

        if(twoHead != None):
            oneTail.next = twoHead
    else:
        # One wali list is empty
        if(twoHead != None):
            zeroTail.next = twoHead

    # Remove zeroHead dummy node
    temp = zeroHead
    zeroHead = zeroHead.next
    temp.next = None
    del temp
        
    # return head of the modified linked list
    return zeroHead
    
head = Node(2)
second = Node(2)
third = Node(0)
fourth = Node(1)
fifth = Node(0)
sixth = Node(0)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("input LL: ")
printList(head)

# sortZeroOneTwo(head)
# print("printing the sorted list ")
# printList(head)

temp = None
head = sort2(head) # by creation of 3 separate list
print("Came out of sort function")
printList(head)
   
