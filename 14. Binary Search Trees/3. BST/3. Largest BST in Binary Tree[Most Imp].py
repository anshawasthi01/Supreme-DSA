class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeData:
    def __init__(self, size=None, maxVal=None, minVal=None, validBST=None):
        self.size = size
        self.maxVal = maxVal
        self.minVal = minVal
        self.validBST = validBST

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

def findLargestBST(root, ans):
    # base case
    if root is None:
        temp = NodeData(0, float('-inf'), float('inf'), True)
        return temp

    leftKaAns = findLargestBST(root.left, ans)
    rightKaAns = findLargestBST(root.right, ans)

    # checking starts here
    currNodeKaAns = NodeData()

    currNodeKaAns.size = leftKaAns.size + rightKaAns.size + 1
    currNodeKaAns.maxVal = max(root.data, rightKaAns.maxVal)
    currNodeKaAns.minVal = min(root.data, leftKaAns.minVal)

    if leftKaAns.validBST and rightKaAns.validBST and (root.data > leftKaAns.maxVal and root.data < rightKaAns.minVal):
        currNodeKaAns.validBST = True
    else:
        currNodeKaAns.validBST = False

    if currNodeKaAns.validBST:
        ans[0] = max(ans[0], currNodeKaAns.size)

    return currNodeKaAns

root = Node(50)
first = Node(30)
second = Node(60)
third = Node(5)
fourth = Node(20)
fifth = Node(45)
sixth = Node(70)
seventh = Node(65)
eight = Node(80)

root.left = first
root.right = second
first.left = third
first.right = fourth
second.left = fifth
second.right = sixth
sixth.left = seventh
sixth.right = eight

print("Printing the tree:")
levelOrderTraversal(root)

ans = [0]
findLargestBST(root, ans)
print("Largest BST size:", ans[0])
