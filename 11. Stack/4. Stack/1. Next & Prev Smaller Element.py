from typing import List

def prevSmallerElement(input: List[int]) -> List[int]:
    s = [-1]
    ans = [0] * len(input)
    
    # left to right -> prev smaller
    for i in range(len(input)):
        curr = input[i]
        
        # apka answer stack me
        while s[-1] >= curr:
            s.pop()
            
        # chotta element mil chuka h -> ans store
        ans[i] = s[-1]
        
        # push krdo curr element ko
        s.append(curr)
        
    return ans


def nextSmaller(input: List[int]) -> List[int]:
    s = [-1]
    ans = [0] * len(input)
    
    for i in range(len(input)-1, -1, -1):
        curr = input[i]
        
        # apka answer stack me
        while s[-1] >= curr:
            s.pop()

        # chotta element mil chuka h -> ans store    
        ans[i] = s[-1]
        
        # push krdo curr element ko
        s.append(curr)
        
    return ans


input = [2, 1, 4, 3]

ans1 = nextSmaller(input)
print("Printing ans1")
print(*ans1)

ans2 = prevSmallerElement(input)
print("Printing ans2")
print(*ans2)
