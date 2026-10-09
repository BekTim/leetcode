def multiplier(i,k):
    while s[i] != "]" and cnt != 0:
        print(i,k)
        break

s = "3[a2[c]]"
print("c" * 2)
# 3 * (a * (2 * c))
cnt = 0
res = []
arrtemp = []
i = 0
k = 0

while i < len(s):
    if s[i] == "[" or s[i].isdigit or 'a' <= s[i] <= 'z':
        res.append(s[i])
    elif s[i] == "]":
        while 
