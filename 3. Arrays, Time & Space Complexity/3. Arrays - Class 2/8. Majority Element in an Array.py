# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# CodeHelp
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s, e = 0, len(arr)-1

        while s < e:
            mid = s + (e - s)//2
            if arr[mid] < arr[mid+1]:
                s = mid + 1
            else:
                e = mid
        
        return e
        return s


            