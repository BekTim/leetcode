s = "keiou"
k = 2
i = 0
j = 0
subs = s[:k]
cnt = 0
cntCompare = float('inf')

vowels = ['a','e','i','o','u']

while i < len(subs):
    while j < len(vowels):
        if vowels[j] == subs[i]:
            cnt += 1
        j = j + 1
    i = i + 1
print(cnt)