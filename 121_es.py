prices = [7,6,4,3,1]

r = len(prices)-1
res = 0
res2 = float('-inf')
for l in range(len(prices)):
    while r != l:
        res = prices[r] - prices[l]
        if res >= res2:
            res2 = res
        r -= 1
    r = len(prices) - 1

if res2 <= 0:
    res2 = 0
    
print(res2)
