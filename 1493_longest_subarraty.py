nums = [0,1,1,1,0,1,1,0,1]
l,r,cnt,res = 0,0,0,0

while r < len(nums):
    if nums[r] == 0:
        l += 1
        j = r + 1
        while j < len(nums):
            if nums[j] == 1:
                cnt +=1 
            else:
                cnt 
    
    pass

    
    

'''
if nums[r] == 1:
        cnt += 1
    elif nums[r] == 0 or r+1 >= len(nums):
        res = max(res, cnt)
        cnt = 0
    r += 1

print(res)
'''