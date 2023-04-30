from typing import List
import sys

def prev_smaller_element(input: List[int]) -> List[int]:
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

def next_smaller(input: List[int]) -> List[int]:
    s = [-1]
    ans = [0] * len(input)

    for i in range(len(input)-1, -1, -1):
        curr = input[i]

        # apka answer stack me 
        while s[-1] != -1 and input[s[-1]] >= curr:
            s.pop()

        # chotta element mil chuka h -> ans store
        ans[i] = s[-1]

        # push krdo curr element ko
        s.append(i)
    return ans

def get_rectangular_area_histogram(height: List[int]) -> int:
    # step1: prevSmaller output
    prev = prev_smaller_element(height)

    # step2: nextSmaller call
    next = next_smaller(height)

    max_area = -sys.maxsize
    size = len(height)

    for i in range(len(height)):
        length = height[i]

        if next[i] == -1:
            next[i] = size

        width = next[i] - prev[i] - 1

        area = length * width
        max_area = max(max_area, area)

    return max_area

if __name__ == '__main__':
    v = [2, 1, 5, 6, 2, 3]

    print(f"Ans is: {get_rectangular_area_histogram(v)}")
