from collections import Counter


arr = "a a a z"

x = arr.split()
print(x)
x = Counter(x)
print(x)
print(x.most_common(1)[0][0])