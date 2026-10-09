s = "leet**cod*e"
s = list(s)
i = 0
cnt = 0
while i < len(s):
    if s[i] == "*":
        cnt += 1
    if cnt >= 1:
        s.pop(i)
        s.pop(i - 1)
        cnt -= 1
        i = i - 2

    i = i + 1
    print(s)