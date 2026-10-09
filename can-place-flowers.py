flowerbed = [1,0,0,0,1]
n = 1
i = 0
cnt = 0

is_active = False
 

len1 = len(flowerbed)

while i < len1:
    if i < len1 and i+1 < len1 and i+2 <len1 and flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
        cnt = cnt + 1
        i = i + 2
        if cnt == n:
            is_active = True
            break
    else: 
        is_active = False
        i = i + 1

print(is_active)
        

# solved by myself!!!!