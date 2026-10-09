candies = [2, 3, 5, 1, 3]
extracandies = 3

greatest = max(candies)

result = []

for candy in candies:
    if candy + extracandies >= greatest:
        result.append(True)
    else: result.append(False)

print(result)