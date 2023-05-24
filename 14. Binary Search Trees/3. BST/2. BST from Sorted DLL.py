class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bstUsingInorder(inorder, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    element = inorder[mid]
    root = Node(element)

    root.left = bstUsingInorder(inorder, start, mid - 1)
    root.right = bstUsingInorder(inorder, mid + 1, end)

    return root


from queue import Queue
def levelOrderTraversal(root):
    q = Queue()
    # initially
    q.put(root)
    q.put(None)

    while not q.empty():
        # A
        temp = q.get()
        # B
        if temp is None:
            print()
            if not q.empty():
                q.put(None)
        else:
            # C
            print(temp.data, end=" ")
            # D
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)

def convert_into_sorted_dll(root, head):
    # base case
    if root is None:
        return head

    # right subtree into LL
    head = convert_into_sorted_dll(root.right, head)

    # attach root node
    root.right = head

    if head is not None:
        head.left = root

    # update head
    head = root

    # left subtree linked List
    head = convert_into_sorted_dll(root.left, head)
    return head

def print_linked_list(head):
    temp = head
    print()
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.right
    print()

def sorted_linked_list_into_bst(head, n):
    if n <= 0 or head_list[0] is None:
        return None

    left_subtree = sorted_linked_list_into_bst(head_list[0], n-1-n//2)

    root = head_list[0]
    root.left = left_subtree

    head_list[0] = head_list[0].right

    # right part solve karna h
    root.right = sorted_linked_list_into_bst(head_list[0], n // 2)
    return root


inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start = 0
end = 8

root = bstUsingInorder(inorder, start, end)
levelOrderTraversal(root)

print("printing sorted linked list:")
head = None
head = convert_into_sorted_dll(root, head)
print_linked_list(head)

head_list = [head]  # Wrap head in a list
root1 =	sorted_linked_list_into_bst(head_list, 9)
print("Doping level order traversal for root 1")
levelOrderTraversal(root1)
