s = "ABBBA"
k = 2
res = []
for l in range(len(s)):
    if len(res) < len(s)/2 and k != 0:
        res.append(s[l])