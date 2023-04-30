def insertAtBottom(s, target):
    # base case
    if not s:
        s.append(target)
        return

    topElement = s.pop()
    # recursive call
    insertAtBottom(s, target)
    # backtracking
    s.append(topElement)


def reverseStack(s):
    # base case
    if not s:
        return

    target = s.pop()

    # reverse stack
    reverseStack(s)
    # insert at bottom target ko
    insertAtBottom(s, target)


if __name__ == '__main__':
    s = [10, 20, 30, 40, 50]

    reverseStack(s)

    print("Printing")
    while s:
        print(s[-1], end=" ")
        s.pop()
    print()
