word1 = "abc"
word2 = "bca"
word1 = set(word1)
word2 = set(word2)
cnt = 0
saver = {}
if len(word1) != len(word2):
    print(False)
else:
    while word1 != word2:
        for i in range(len(word1)):
            if word1[i] in word2:
                saver[cnt] = word1[i]
                cnt += 1
                print(cnt)
            elif cnt == 2:
                word1[i] = saver[cnt]
                print(word1[i])
                