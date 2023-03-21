def printSubArray_util(nums, start, end):
    # base
    if end == len(nums):
        return

    # 1 case solve
    for i in range(start, end+1):
        print(nums[i], " ", end = ' ')

    print()

    # RE
    printSubArray_util(nums, start, end + 1)

def printSubArray(nums):
    for start in range(len(nums)):
        end = start
        printSubArray_util(nums, start, end)

nums = [1, 2, 3, 4, 5]
printSubArray(nums)

