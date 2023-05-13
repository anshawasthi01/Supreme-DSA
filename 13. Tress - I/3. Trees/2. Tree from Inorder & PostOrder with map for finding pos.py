class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createMapping(mapping, inorder, n):
    for i in range(n):
        mapping[inorder[i]] = i


def buildTreeFromPostOrderInOrder(inorder, postorder, postIndex, size, inorderStart, inorderEnd, mapping):
    # base case
    if postIndex[0] < 0 or inorderStart > inorderEnd:
        return None

    # A
    element = postorder[postIndex[0]]
    postIndex[0] -= 1
    root = Node(element)

    # B: root.right solve
    # pos = findPosition(inorder,size, element)
    pos = mapping[element]
    root.right = buildTreeFromPostOrderInOrder(inorder, postorder, postIndex, size, pos+1, inorderEnd, mapping)
    # C: root.left solve
    root.left = buildTreeFromPostOrderInOrder(inorder, postorder, postIndex, size, inorderStart, pos-1, mapping)

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



inorder = [40,20,10,50,30,60]
postorder = [40,20,50,60,30,10]
size = 6
postIndex = [size-1]
inorderStart = 0
inorderEnd = size-1

mapping = {}

createMapping(mapping, inorder, size)

print("Building the tree:")
root = buildTreeFromPostOrderInOrder(inorder, postorder, postIndex, size, inorderStart, inorderEnd, mapping)

print("Printing the tree:")
levelOrderTraversal(root)