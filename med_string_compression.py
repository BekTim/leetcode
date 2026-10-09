chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c"]
s = []
cnt = 0
startPos = -1
j = 0
for i in range(len(chars)):
    if i < len(chars)-1 and chars[i] == chars[i+1]:
        startPos = i
        print(startPos)
        while j+1 < len(chars) and chars[startPos] == chars[j+1]:    
            cnt += 1
            j += 1
        
        i = j
    else:
        s.append(chars[i])

    s.append(chars[j])
    s.append(cnt)
    
    print(s)


