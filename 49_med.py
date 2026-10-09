from collections import Counter

strs = ["eat","tea","tan","ate","nat","bat"]
t = []

for i in range(len(strs)):
    if strs[i] not in t:
        t.append(strs[i])
    for j in range(i+1, len(strs)):
        if Counter(strs[i]) == Counter(strs[j]) and strs[j] not in t :
            t.append(strs[j])

print(t)

