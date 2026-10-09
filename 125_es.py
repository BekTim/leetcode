s = " "
s = s.lower()
m = []

for l in range(len(s)):
    if s[l].isalnum():
        m.append(s[l])

r = len(m) - 1

if len:
    print(True)

for l in range(len(m)):
    if m[l] == m[r]:
        print("perfect: ", m[l], m[r])
        r-=1
    else:
        print("breaked at:", m[l], m[r])
        r-=1
