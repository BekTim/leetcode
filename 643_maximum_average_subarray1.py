nums = [5]
k = 1
devisNum = k
i = 0
j = 1
res = 0
res2 = 0
while i < k and k <= len(nums):
    res = nums[i]
    while j < k:
        res += nums[j]
        j = j + 1
    i = i + 1
    j = i + 1
    k = k + 1
    res = res / devisNum
    if res < res2:
        res = res2
    res2 = res

print(res)