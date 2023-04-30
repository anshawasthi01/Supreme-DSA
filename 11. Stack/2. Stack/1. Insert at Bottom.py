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


if __name__ == '__main__':
    s = [10, 20, 30, 40, 50, 60, 70]

    if not s:
        print("Stack is empty, can't insert at bottom")
        exit()

    target = s.pop() # we can take any value
    insertAtBottom(s, target)

    print("Printing")
    while s:
        print(s[-1], end=" ")
        s.pop()
    print()
