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

def minVal(root):
    temp = root
    if temp is None:
        return -1

    while temp.left is not None:
        temp = temp.left
    return temp.data


def maxVal(root):
    temp = root
    if temp is None:
        return -1

    while temp.right is not None:
        temp = temp.right
    return temp.data


# 10 20 5 11 17 2 4 8 6 25 15 -1

print("Enter the data for Node")
root = takeInput()
print(" Minimum value: ", minVal(root))
print("Maximum value: ", maxVal(root))

