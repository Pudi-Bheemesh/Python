str = input("Enter String: ")
Vow = Con = Dig = Spa = spl = 0

for i in str:
    if i.isalpha():
        if i == 'a' or i == 'e' or i == 'i' or i == 'i' or i == 'u':
            Vow += 1
        else:
            Con += 1
    if i == ' ':
        Spa += 1
    if i.isdigit():
        Dig += 1
    if i == '#' or i == '@' or i == '/' or i == '$':
        spl += 1

print ("Vowels = ",Vow)
print ("Consonants = ",Con)
print ("Digits = ",Dig)
print ("Space = ",Spa)
print ("Special character = ",spl)
