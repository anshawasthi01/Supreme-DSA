# https://practice.geeksforgeeks.org/problems/quick-sort/1

# CodeHelp

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self, a, s, e):
        
        if s >= e: return
        pivot, i, j = e, s - 1, s
        
        while j < pivot:
            if a[j] < a[pivot]:
                i += 1
                a[i], a[j] = a[j], a[i]
            j += 1
        i += 1
        
        # i is the right position for the pivot element
        a[i], a[pivot] = a[pivot], a[i]
        self.quickSort(a, s, i - 1)
        self.quickSort(a, i + 1, e)
        # code here
    
    def partition(self,arr,low,high):
        pass