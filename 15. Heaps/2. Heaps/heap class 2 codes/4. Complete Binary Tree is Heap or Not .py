class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solve(root):
    # Base case
    if root is None:
        return True, float('-inf')
    
    if root.left is None and root.right is None:
        # Leaf node
        return True, root.data
    
    leftAns = solve(root.left)
    rightAns = solve(root.right)

    if (leftAns[0] and rightAns[0] and root.data > leftAns[1] and root.data > rightAns[1]):
        return True, root.data
    else:
        return False, root.data

# Example usage
root = Node(50)
root.left = Node(30)
root.right = Node(90)
root.left.left = Node(10)
root.left.right = Node(20)

isHeap = solve(root)

if isHeap[0]:
    print("The given binary tree is a heap.")
else:
    print("The given binary tree is not a heap.")
