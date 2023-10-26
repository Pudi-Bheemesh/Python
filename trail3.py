n = int(input("Enter your length"))
string = input("Enter your sentence: ")
words = []
string = string.split()
for i in range(len(string)):
    if len(string[i]) > n:
        words.append(string[i])
print(words)