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


def maxVal(root):
    temp = root
    if temp is None:
        return -1

    while temp.right is not None:
        temp = temp.right
    return temp.data

def deleteNodeInBST(root, target):
    # base case
    if root is None:
        return None

    # print("Request recieved for ", root.data, " with target", target)
    # print()
    if root.data == target:
        # isi ko delete krna h 
        # 4 cases 
        if root.left is None and root.right is None:
            # leaf node
            # del root
            return None
        elif root.left is None and root.right is not None:
            child = root.right
            # del root
            return child
        elif root.left is not None and root.right is None:
            child = root.left
            # del root
            return child
        else:
            # both child
            # find inorder predecessor in left subtree
            inorderPre = maxVal(root.left)
            # replace root.data value with inorder predecessor
            root.data = inorderPre
            # delete inorder predecessor from left subtree
            root.left = deleteNodeInBST(root.left, inorderPre)
            return root
    elif target > root.data:
        # right jana chahiye
        root.right = deleteNodeInBST(root.right, target)
    elif target < root.data:
        # left jana chahioye
        root.left = deleteNodeInBST(root.left, target)
    return root

# 100 50 150 40 60 175 110 -1

print("Enter the data for Node")
root = takeInput()
print()
print("Printing the tree")
levelOrderTraversal(root)
print()
root = deleteNodeInBST(root, 100)
levelOrderTraversal(root)