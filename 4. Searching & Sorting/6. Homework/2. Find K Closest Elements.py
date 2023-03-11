# https://leetcode.com/problems/find-k-closest-elements/

def lowerBound(arr, x):
    start, end = 0, len(arr) - 1
    ans = end
    while start <= end:
        mid = (start+end)//2
        if arr[mid] >= x:
            ans = mid
            end = mid - 1
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return ans

def bs_method(arr, k, x):
    # lower bound
    h = lowerBound(arr, x)
    l = h - 1
    while k > 0:
        if l < 0:
            h += 1
        elif h >= len(arr):
            l -= 1
        elif x - arr[l] > arr[h] - x:
            h += 1
        else:
            l -= 1
    ans = []

    for i in range(1, h+1):
        ans.append(arr[i])
    return ans

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Code Help
        bs_method(arr, k, x)
