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
    
    
def storeSuggestions(curr, temp, prefix):
    if curr.isTerminal:
        temp.append(prefix)

    # a to z tak choices dedo
    for ch in range(ord('a'), ord('z')+1):
        index = ch - ord('a')

        Next = curr.children[index]

        if Next is not None:
            # If child exists
            prefix += chr(ch)
            storeSuggestions(Next, temp, prefix)
            prefix = prefix[:-1]


def getSuggestions(root, input):
  # var/DS
    prev = root
    output = []
    prefix = ""
    
    for i in range(len(input)):
        lastch = input[i]

        index = ord(lastch) - ord('a')
        curr = prev.children[index]

        if curr is None:
            break
        else:
            # iske andar main saare suggestion store krke launga
            temp = []
            prefix += lastch
            storeSuggestions(curr, temp, prefix)
            output.append(temp)
            prev = curr
    
    return output


v = ["love", "lover", "loving", "last", "lost", "lane", "lord"]
input_str = "lovi"

root = TrieNode('-')
for word in v:
    insertWord(root, word)

ans = getSuggestions(root, input_str)

print("Printing the answer:")
for suggestions in ans:
    for suggestion in suggestions:
        print(suggestion, end=", ")
    print()
