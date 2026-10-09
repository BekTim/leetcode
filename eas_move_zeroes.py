nums = [1,2,3,1]
# nums = [1,0,0,3,12]
i,j = 0,0
perm = 1
while j < len(nums):
    while i < len(nums) and i+1 < len(nums):
        if nums[i] <= nums[i+1] and (nums[i] == 0 or nums[i+1] == 0):
            perm = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = perm
        i = i+1
    print(nums)
    i = 0
    j = j + 1

# nums = [0,1,0,3,12]
# nums = [1,0,0,3,12]