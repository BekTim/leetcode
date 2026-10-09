nums = [0,0]
target = 7

for i in range(len(nums)):
    for j in range(i+1 ,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)

        