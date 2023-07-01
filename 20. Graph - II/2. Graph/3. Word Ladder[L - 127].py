# https://leetcode.com/problems/word-ladder/

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # <pair<string, int> >
        q = deque()
        q.append((beginWord, 1))
        st = set(wordList)
        # jo bhi word queue me insert karunga, toh usko set me se remove krdunga
        st.discard(beginWord)

        while q:
            currString, currCount = q.popleft()

            # check kahin destination tak toh nahi pohoch gye
            if currString == endWord:
                return currCount

            for index in range(len(currString)):
                # hr index pr jo value h, usko main 'a' to 'z' se replace karunga
                originalCharacter = currString[index]

                # Replace the character at the current index with all possible characters
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    currString = currString[:index] + ch + currString[index + 1:]

                    # Check if the modified string is in the wordList
                    if currString in st:
                        q.append((currString, currCount + 1))
                        st.remove(currString)

                    # bringing back the currString to its original State
                    currString = currString[:index] + originalCharacter + currString[index + 1:]

        return 0






















    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # Create a set of words for faster lookup
    #     wordSet = set(wordList)
    #     if endWord not in wordSet:
    #         return 0
        
    #     # Initialize queue with the beginWord and set of visited words
    #     queue = deque([(beginWord, 1)])
    #     visited = set([beginWord])
        
    #     while queue:
    #         # Dequeue the word and its level
    #         word, level = queue.popleft()
            
    #         # Iterate over each character in the word
    #         for i in range(len(word)):
    #             # Iterate over all possible lowercase letters
    #             for c in 'abcdefghijklmnopqrstuvwxyz':
    #                 # Skip if the character is the same as in the original word
    #                 if c == word[i]:
    #                     continue
                    
    #                 # Create the new word by replacing the character at index i
    #                 newWord = word[:i] + c + word[i+1:]
                    
    #                 # Check if the new word is in the wordSet and has not been visited before
    #                 if newWord in wordSet and newWord not in visited:
    #                     # Check if the new word is the endWord
    #                     if newWord == endWord:
    #                         return level + 1
                        
    #                     # Enqueue the new word and its level
    #                     queue.append((newWord, level + 1))
                        
    #                     # Add the new word to the set of visited words
    #                     visited.add(newWord)
        
    #     # No transformation sequence exists
    #     return 0