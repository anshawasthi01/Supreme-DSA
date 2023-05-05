# https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1

# CodeHelp
from queue import Queue

def solve(str):
    freq = [0] * 26
    q = Queue()

    ans = ""

    for ch in str:
        # increment frequency
        freq[ord(ch) - ord('a')] += 1
        # enqueue
        q.put(ch)

        while not q.empty():
            if freq[ord(q.queue[0]) - ord('a')] > 1:
                q.get()
            else:
                ans += q.queue[0]
                break

        if q.empty():
            ans += '#'

    # print("Final Ans: " + ans)
    return ans

class Solution:
	def FirstNonRepeating(self, A):
		return solve(A)