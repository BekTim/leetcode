vowels = {'a' ,'e','i','o','u','A','E','I','O','U'}
s = "IceCreAm"
s = list(s)
i,j = 0, len(s) - 1

while i < j:
    if s[i] not in vowels:
        i = i + 1
    if s[j] not in vowels:
        j = j - 1
    else:
        s[i], s[j] = s[j], s[i]
        i = i + 1
        j = j - 1
    
print(s)
    