import re
n = int(input("Enter your number: "))
i = 0
lst = []
while i < n:
    item = input()
    lst = lst + [item]
    i += 1
USNRegex = re.compile(r'\d\w\w\d\d\w\w\d\d\d')
i = 0
for i in lst:
    if USNRegex.search(i) != None:
        print(i)
