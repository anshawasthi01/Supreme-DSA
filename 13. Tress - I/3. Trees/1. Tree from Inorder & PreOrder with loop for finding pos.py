class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_position(arr, n, element):
    for i in range(n):
        if arr[i] == element:
            return i
    return -1

# build tree from inorder and preorder traversal
def buildTreeFromPreOrderInOrder(inorder, preorder, size, preIndex, inorderStart, inorderEnd):
    # Base case
    if preIndex[0] >= size or inorderStart > inorderEnd:
        return None

    # Step A:
    element = preorder[preIndex[0]]
    preIndex[0] += 1
    root = Node(element)
    pos = find_position(inorder, size, element)

    # Step B: root.left solve
    root.left = buildTreeFromPreOrderInOrder(inorder, preorder, size, preIndex, inorderStart, pos-1)
    # Step C: root.right solve
    root.right = buildTreeFromPreOrderInOrder(inorder, preorder, size, preIndex, pos+1, inorderEnd)

    return root

from queue import Queue
def levelOrderTraversal(root):
    q = Queue()
    # initially
    q.put(root)
    q.put(None)

    while not q.empty():
        # A
        temp = q.get() #front
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

inorder = [40,20,50,10,60,30,70]
preorder = [10,20,40,50,30,60,70]
size = 7
preIndex = [0]
inorderStart = 0
inorderEnd = size-1
print("Building Tree: ")
root = buildTreeFromPreOrderInOrder(inorder, preorder, size, preIndex, inorderStart, inorderEnd )
print()
print("Printing level order traversal ")
levelOrderTraversal(root)
