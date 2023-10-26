n = int(input("Enter total num: "))
num = input("Enter numbers: ")
even = 0
odd = 0
a = num.split(" ")
for i in range(0,len(a)):
    if int(a[i])%2==0:
        even=even+1
    else:
        odd=odd+1
print(even,"",odd)