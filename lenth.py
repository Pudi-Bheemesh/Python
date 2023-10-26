n = int(input())
sentence = input()
long_word = []
txt = sentence.split(" ")
for i in txt:
    if len(i)>n:
        long_word.append(i)

print(long_word)