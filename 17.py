from collections import Counter
arr = [8, 5, 12, 8, 5, 8]
d = Counter(arr)

for i,j in d.items():
    if j > 1:
        print(i)