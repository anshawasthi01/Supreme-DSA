# https://leetcode.com/problems/largest-rectangle-in-histogram/ [Hard]

# CodeHelp

class Solution:
    def prevSmallerElement(self, input: List[int]) -> List[int]:
        s = [-1]
        ans = [0] * len(input)

        # left to right -> prev smaller
        for i in range(len(input)):
            curr = input[i]

            # apka answer stack me
            while s[-1] != -1 and input[s[-1]] >= curr:
                s.pop()

            # chotta element mil chuka h -> ans store
            ans[i] = s[-1]

            # push krdo curr element ko
            s.append(i)

        return ans

    def nextSmaller(self, input: List[int]) -> List[int]:
        s = [-1]
        ans = [0] * len(input)

        for i in range(len(input) - 1, -1, -1):
            curr = input[i]

            # apka answer stack me
            while s[-1] != -1 and input[s[-1]] >= curr:
                s.pop()

            # chotta element mil chuka h -> ans store
            ans[i] = s[-1]

            # push krdo curr element ko
            s.append(i)

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        # step1: prevSmaller output
        prev = self.prevSmallerElement(heights)

        # step2: nextSmaller call
        next = self.nextSmaller(heights)

        maxArea = float('-inf')
        size = len(heights)

        for i in range(len(heights)):
            length = heights[i]

            if next[i] == -1:
                next[i] = size

            width = next[i] - prev[i] - 1

            area = length * width
            maxArea = max(maxArea, area)

        return maxArea
