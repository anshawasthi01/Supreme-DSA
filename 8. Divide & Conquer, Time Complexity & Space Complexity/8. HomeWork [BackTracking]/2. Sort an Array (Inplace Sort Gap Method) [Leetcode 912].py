# https://leetcode.com/problems/sort-an-array/
# https://codeshare.io/OdxpvW   (Class Code)

# Code Help Inplace Sorting
def mergePlace(arr, start, mid, end):
    total_len = end - start + 1
    gap = total_len // 2 + total_len % 2 # Ceil

    while gap > 0:
        i, j = start, start + gap
        while j <= end:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        gap = 0 if gap <= 1 else (gap // 2) + (gap % 2)

def mergeSort(arr, start, end ):
    if start >= end: return
    # mid = start + (end - start) // 2
    mid = (start + end) >> 1

    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    mergePlace(arr, start, mid, end)


class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        mergeSort(arr, 0, len(arr) - 1 )
        return arr

