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

def inorderTraversal(root):
    # base case
    if root is None:
        return

    # LNR
    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


def preorderTraversal(root):
    # base case
    if root is None:
        return

    # NLR
    print(root.data, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)


def postorderTraversal(root):
    if root is None:
        return

    # LRN
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")


root = buildTree()
# inorderTraversal(root)
# preorderTraversal(root)
postorderTraversal(root)