from collections import Counter
str = input("Enter input: ")
test = str.split()
test.sort()
UniqW = Counter()
res= "".join(UniqW.keys())
print (res)