class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree():
    data = int(input("Enter the data: "))

    if data == -1:
        return None

    # Step A , B and C
    root = Node(data)

    print(f"Enter data for left part of {data} node")
    root.left = buildTree()

    print(f"Enter data for right part of {data} node")
    root.right = buildTree()

    return root


#         1
#       /   \
#      2     3
#     / \
#    4   5
#   k = 1
#   p = 4
def kthAncestor(root, k, p):
    # base case
    if not root:
        return False

    if root.data == p:
        return True

    leftAns = kthAncestor(root.left, k, p)
    rightAns = kthAncestor(root.right, k, p)

    # wapas aare honge
    # check left ya right me answer mila ya anhi
    if leftAns or rightAns:
        k -= 1
    if k == 0:
        print(f"Answer: {root.data}")
        k = -1

    return leftAns or rightAns


if __name__ == "__main__":
    root = buildTree()
    k = 1
    p = 4
    found = kthAncestor(root, k, p)
