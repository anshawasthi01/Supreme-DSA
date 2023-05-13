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

from typing import Dict
from collections import deque

def printBottomView(root):
    if root is None:
        return

    # create a dict for storing HD -> TopNode -> data
    topNode = {}

    # Level Order
    # we will store a tuple consisting of Node and Horizontal Distance
    q = deque([(root, 0)])

    while q:
        frontNode, hd = q.popleft() # horizontal distance

        # # jo bhi horizontal distance aaya h , check if answer for that hd already exists
        # # or not
        # if hd not in topNode: these 3 lines for top view
        # create entry
        topNode[hd] = frontNode.data

        if frontNode.left:
            q.append((frontNode.left, hd-1))

        if frontNode.right:
            q.append((frontNode.right, hd+1))

    # ab aapka answer store hua hoga aapke dict me
    print("Printing the answer:")
    for hd, node in sorted(topNode.items()):
        print(hd, "->", node)

root = buildTree()
printBottomView(root)

# Input : 10, 20, 30, -1, -1, 40, 60, -1, -1, -1, 80, 50, -1, 70, -1, -1, 90, -1, -1


