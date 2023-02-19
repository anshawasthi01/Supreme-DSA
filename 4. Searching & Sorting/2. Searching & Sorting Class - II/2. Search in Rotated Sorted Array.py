# https://leetcode.com/problems/search-in-rotated-sorted-array/


# Modified Element

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start, end = 0, len(nums)-1

#         while start<=end:
#             m = start+(end-start)//2

#             if nums[m]==target:
#                 return m

#             if nums[start] <= nums[m]:
#                 if target >= nums[start] and target < nums[m]:
#                     end = m-1
#                 else:
#                     start+=1
#             else:
#                 if target <= nums[end] and target > nums[m]:
#                     start = m+1
#                 else:
#                     end = m-1
#         return -1


def binarySearch(arr, target, start, end):
    mid = start + (end - start ) // 2
    while start <= end:
        element = arr[mid]

        if element == target: # element found, then return index
            return mid

        if target < element:
            # search in left
            end = mid - 1
        
        else:
            # search in right
            start = mid + 1
            mid = start + (end - start) // 2
    # element not found
    return -1

def findPivot(arr):
    s, e = 0, len(arr)-1 
    while s <= e:
        mid = s + (e-s)//2

        if mid+1 < len(arr) and arr[mid] > arr[mid+1]:
            return mid

        if mid-1 >= 0 and arr[mid-1] > arr[mid]:
            return mid - 1

        if arr[s] >= arr[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return s

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivotIndex = findPivot(nums)

        if target >= nums[0] and target <= nums[pivotIndex]:
            # search in array A
            ans = binarySearch(nums, target, 0, pivotIndex)
            return ans
        
        if pivotIndex+1 < len(nums) and target >= nums[pivotIndex+1] and target <= nums[len(nums)-1]:
            # search in array B
            ans = binarySearch(nums, target, pivotIndex+1, len(nums)-1)
            return ans
        return -1




















# Modified Element

        # start, end = 0, len(nums)-1

        # while start<=end:
        #     m = start+(end-start)//2

        #     if nums[m]==target:
        #         return m

        #     if nums[start] <= nums[m]:
        #         if target >= nums[start] and target < nums[m]:
        #             end = m-1
        #         else:
        #             start+=1
        #     else:
        #         if target <= nums[end] and target > nums[m]:
        #             start = m+1
        #         else:
        #             end = m-1
        # return -1





# class Solution {
# public:
#     int binarySearch(vector<int> arr, int target, int start, int end) {

#     int mid = start + (end - start ) / 2;

#     while(start <= end) {
#         int element = arr[mid];

#         if(element == target) {//element found, then return index
#         return mid;
#         }
        
#         if(target < element) {
#         //search in left
#         end = mid - 1;
#         }
#         else {
#         //search in right
#         start = mid + 1;
#         }

#         mid = start + (end - start ) / 2;

#     }

#   //element not found
#   return -1;

# }
#     int findPivot(vector<int> arr) {
#     int s = 0;
#     int e = arr.size() - 1;
#     int mid = s + (e-s)/2;

#     while(s < e) {
#         if(mid+1 < arr.size() && arr[mid] > arr[mid+1])
#         return mid;
#         if(mid-1 >= 0 && arr[mid-1] > arr[mid])
#         return mid-1;

#         if(arr[s] >= arr[mid])
#         e = mid - 1;
#         else
#         s = mid ;
#         mid = s + (e-s)/2;
#     }
#     return s; 
#     }

#     int search(vector<int>& nums, int target) {
#         int pivotIndex = findPivot(nums);

#         if(target >= nums[0] && target <= nums[pivotIndex]){
#             //search in array A
#             int ans = binarySearch(nums, target, 0, pivotIndex);
#             return ans;
#         }

#         if(pivotIndex+1 < nums.size() && 
#         target >= nums[pivotIndex+1] && target <= nums[nums.size()-1]){
#             //search in array B
#             int ans = binarySearch(nums, target, pivotIndex+1, nums.size()-1);
#             return ans;
#         }
#         return -1;
        
#     }
# };


















































