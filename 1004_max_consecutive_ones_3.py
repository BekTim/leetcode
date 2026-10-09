nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
l, cnt0, cnt1 = 0,0,0
max_val = 0
max_val2 = 0
for r in range(len(nums)):
    if nums[r] == 0 and r < k:
        cnt0 += 1
        cnt1 += 1
    if cnt0 == k:
        l += 1
        r = l - 1
        cnt0 = 0
        max_val = cnt1
        cnt1 = 0
    if nums[r] == 1:
        cnt1 += 1
    print(cnt1)
    max_val2 = max(max_val, max_val2)

print(max_val2)


'''
for i in len(nums):
    if nums[i] == 0 and cnt0 < k:
        cnt0 += 1
        cnt1 += 1
        if cnt0 == k:

    elif nums[i] == 1:
        cnt1 += 1
    
'''