class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertIntoBST(root, data):
    if root is None:
        # this is the first node we have to create
        root = Node(data)
        return root
    
    # not the first node
    if root.data > data:
        # insert in left
        root.left = insertIntoBST(root.left, data)
    else:
        # insert in right
        root.right = insertIntoBST(root.right, data)
    
    return root


def takeInput():
    root = None
    data = int(input())
    
    while data != -1:
        root = insertIntoBST(root, data)
        data = int(input())
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

def preOrderTraversal(root):
    # NLR
    if root is None:
        return
    
    print(root.data, end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def inOrderTraversal(root):
    # LNR
    if root is None:
        return
    
    inOrderTraversal(root.left)
    print(root.data, end=' ')
    inOrderTraversal(root.right)


def postOrderTraversal(root):
    # LRN
    if root is None:
        return
    
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=' ')


# 10 20 5 11 17 2 4 8 6 25 15 -1

print("Enter the data for Node")
root = takeInput()
print("Printing the tree")
levelOrderTraversal(root)
print()
print("Printing Inorder:")
inOrderTraversal(root)
print()
print("Printing Preorder:")
preOrderTraversal(root)
print()
print("Printing Postorder:")
postOrderTraversal(root)

