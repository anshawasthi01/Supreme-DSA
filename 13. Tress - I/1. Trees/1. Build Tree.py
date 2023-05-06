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

buildTree()