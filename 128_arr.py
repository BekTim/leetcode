nums = [1,0,1,2]
if not nums:
    print(0)
else:
    nums = sorted(nums)
    i = 0
    cnt = 1
    cnt1 = 0

    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            i += 1
        elif nums[i] + 1 == nums[i+1]:
            cnt += 1
            i += 1
        else:
            if cnt > cnt1:
                cnt1 = cnt
            cnt = 1
            i += 1

    if cnt > cnt1:
        cnt1 = cnt

    print(cnt1)