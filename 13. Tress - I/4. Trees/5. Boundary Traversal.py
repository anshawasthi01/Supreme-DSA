class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    data = int(input("Enter the data: "))
    if data == -1:
        return None
    
    #Step A, B and C
    root = Node(data)

    print("Enter data for left part of", data, "node:")
    root.left = buildTree()

    print("Enter data for right part of", data, "node:")
    root.right = buildTree()

    return root

def printLeftBoundary(root):
    # base case
    # if root is None, then go back
    if not root:
        return
    # if root is a leaf node, then go back
    if not root.left and not root.right:
        return

    print(root.data, end=" ")

    if root.left:
        printLeftBoundary(root.left)
    else:
        printLeftBoundary(root.right)

def printLeafBoundary(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.data, end=" ")

    printLeafBoundary(root.left)
    printLeafBoundary(root.right)

def printRightBoundary(root):
    # base case
    if not root:
        return
    if not root.left and not root.right:
        return

    if root.right:
        printRightBoundary(root.right)
    else:
        printRightBoundary(root.left)
    
    print(root.data, end=" ")



def boundaryTraversal(root):
    if not root:
        return
    print(root.data, end=" ")
    # A
    printLeftBoundary(root.left)
    # B
    printLeafBoundary(root)
    # C
    printRightBoundary(root.right)


root = buildTree()
boundaryTraversal(root)



# Input : 10 20 30 -1 -1 40 60 -1 -1 -1 80 50 -1 70 -1 -1 90 -1 -1
# 10 20 30 60 70 90 80
# 10 20 30 -1 -1 50 70 90 -1 -1 80 -1 -1 60 -1 -1 40 -1 100 -1 120 110 -1 -1 130 -1 -1 