# https://leetcode.com/problems/distribute-repeating-integers/description/

# CodeHelp

class Solution:
    def canDistributeHelper(self, counts: List[int], quantity: List[int], ithCustomer: int) -> bool:
        # base
        if ithCustomer == len(quantity):
            return True

        for i in range(len(counts)):
            if counts[i] >= quantity[ithCustomer]:
                counts[i] -= quantity[ithCustomer]
                if self.canDistributeHelper(counts, quantity, ithCustomer + 1):
                    return True
                counts[i] += quantity[ithCustomer]  # backtrack
        return False

    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        counts = list(countMap.values())
        quantity.sort(reverse=True)  # sort DESC.
        return self.canDistributeHelper(counts, quantity, 0)
