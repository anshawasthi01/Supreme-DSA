# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# CodeHelp

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''        


def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    ans = None
    if a.data < b.data:
        ans = a
        ans.bottom = merge(a.bottom, b)
    else:
        ans = b
        ans.bottom = merge(a, b.bottom)

    return ans

def flatten(root):
    if not root:
        return None

    mergedLL = merge(root, flatten(root.next))
    return mergedLL