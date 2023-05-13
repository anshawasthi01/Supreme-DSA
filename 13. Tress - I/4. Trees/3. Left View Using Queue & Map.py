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

def printLeftView(root, ans, level):
    # base case
    if not root:
        return
    
    if level == len(ans):
        ans.append(root.data)
        
    # left
    printLeftView(root.left, ans, level + 1)
    # right
    printLeftView(root.right, ans, level + 1)


root = buildTree()
ans = []
level = 0
printLeftView(root, ans, level)
print("Printing the Right View: ")
for i in ans:
    print(i, end=" ")

# Input : 10 20 30 -1 -1 40 60 -1 -1 -1 80 50 -1 70 -1 -1 90 -1 -1