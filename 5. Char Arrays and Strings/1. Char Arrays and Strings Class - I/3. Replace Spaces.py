def Replace(nums):
    for i in range(len(nums)):
        if nums[i] == ' ':
            nums[i] = '@'

st = ['A','N',' ','S','H']
Replace(st)
print(st)