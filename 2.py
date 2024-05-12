num = int(input("Enter the num: "))
temp = num
rev_num = 0

while num > 0:
    ldig = num % 10
    rev_num = (rev_num * 10) + ldig
    num = num // 10

if temp == rev_num:
    print("This number is palindrome")
else:
    print("The number is not palindrome")

str_num = str(temp)
for digit in range(10):
    if str_num.count(str(digit)) != 0:
        print("The count of ", digit,"is: ", str_num.count(str(digit)))