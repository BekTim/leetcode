from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

count = Counter(nums)

sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)

print(sorted_elements[:k])          