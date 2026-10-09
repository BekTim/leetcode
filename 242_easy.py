s = "rat"
t = "car"
cnt = 0
s = sorted(s)
t = sorted(t)

for i in range(len(s)):
    if s[i] == t[i]:
        cnt+=1

if cnt == len(s):
    print(True)
else:
    print(False)