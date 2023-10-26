num = int(input("Enter the number: "))
temp = num
rem = 0
sum = 0
while temp>0:
    rem = temp % 10
    sum = sum+rem*rem*rem
    temp = int(temp / 10)
if sum == num:
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")