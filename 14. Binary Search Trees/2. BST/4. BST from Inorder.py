class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bstUsingInorder(inorder, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    element = inorder[mid]
    root = Node(element)

    root.left = bstUsingInorder(inorder, start, mid - 1)
    root.right = bstUsingInorder(inorder, mid + 1, end)

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


inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start = 0
end = 8

root = bstUsingInorder(inorder, start, end)
levelOrderTraversal(root)
