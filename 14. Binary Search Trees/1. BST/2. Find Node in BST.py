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

# assuming there are only unique values in tree
def findNodeInBST(root, target):
    # base case
    if root is None:
        return None
    
    if root.data == target:
        return root
    # assuming there are only unique values in tree
    # leftAns = false
    # rightAns = false
    if target > root.data:
        # right subtree me search karo
        return findNodeInBST(root.right, target)
    else:
        return findNodeInBST(root.left, target)
    

# 10 20 5 11 17 2 4 8 6 25 15 -1

print("Enter the data for Node")
root = takeInput()
ans  = findNodeInBST(root ,15)
print("present or not : ", ans)
