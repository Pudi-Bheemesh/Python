n = int(input("how many numbers:"))
i = 1
sum = 0
for i in range(1,n):
    cube = i*i*i
    sum = sum + cube


print("the sum of first ",n,"numbers is",sum)