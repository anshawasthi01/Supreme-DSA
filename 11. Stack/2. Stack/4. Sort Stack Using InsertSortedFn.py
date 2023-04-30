def insertSorted(s, target):
    # base case
    if not s:
        s.append(target)
        return
    if s[-1] >= target:
        s.append(target)
        return

    topElement = s.pop()
    insertSorted(s, target)

    # BT
    s.append(topElement)


def sortStack(s):
    # base case
    if not s:
        return

    topElement = s.pop()

    sortStack(s)

    insertSorted(s, topElement)


if __name__ == '__main__':
    s = [7, 11, 3, 5, 9]

    sortStack(s)

    print("Printing")
    while s:
        print(s[-1], end=' ')
        s.pop()
    print()
