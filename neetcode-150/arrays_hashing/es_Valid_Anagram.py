from collections import Counter

s = "racecar"
t = "carrace"
s_counter = Counter(s)
t_counter = Counter(t)


print(s_counter == t_counter)