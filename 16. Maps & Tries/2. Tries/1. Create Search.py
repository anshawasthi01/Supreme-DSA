class TrieNode:
    def __init__(self, d):
        self.data = d
        self.children = [None] * 26
        self.isTerminal = False

def insertWord(root, word):
    # base case
    if len(word) == 0:
        root.isTerminal = True
        return

    ch = word[0]
    index = ord(ch) - ord('a')
    # present
    if root.children[index] is not None:
        child = root.children[index]
    else:
        # not present
        child = TrieNode(ch)
        root.children[index] = child

    # recursion sambhal lega
    insertWord(child, word[1:])

def searchWord(root, word):
    # base case
    if len(word) == 0:
        return root.isTerminal

    ch = word[0]
    index = ord(ch) - ord('a')
    # present
    if root.children[index] is not None:
        child = root.children[index]
    else:
        return False

    # rec call
    return searchWord(child, word[1:])

if __name__ == "__main__":
    root = TrieNode('-')

    insertWord(root, "coding")
    insertWord(root, "code")
    insertWord(root, "coder")
    insertWord(root, "codehelp")
    insertWord(root, "baba")
    insertWord(root, "baby")
    insertWord(root, "babu")
    insertWord(root, "shona")

    print("Searching:")
    if searchWord(root, "cod"):
        print("Present")
    else:
        print("Absent")
