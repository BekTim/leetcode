arr = [-3,0,1,-3,1,1,1,-3,10,0]
arr2 = arr
CntSum = []
cnt = 0
j = 0
for num in arr:
    while j < len(arr2):
        if num == arr2[j]:
            cnt += 1
        j = j + 1
    CntSum.append(cnt)
    j = 0
    cnt = 0

print(len(CntSum) == len(set(CntSum)))