sent = input("Enter your sentence = ")
NoOfWords, NoOfDigits, NoOfUpper, NoOfLower = 0,0,0,0
temp = sent.split()
for word in temp:
    NoOfWords += 1
for i in sent:
    if i.isdigit():
        NoOfDigits += 1
    elif i.isupper():
        NoOfUpper += 1
    elif i.islower():
        NoOfLower += 1

print("Number of words = ", NoOfWords)
print("Number of digits = ", NoOfDigits)
print("Number of Uppercase = ", NoOfUpper)
print("Number of lowercase = ",NoOfLower)