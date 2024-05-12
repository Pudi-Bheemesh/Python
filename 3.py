def fibo(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)

num = int(input("Enter how many numbers: "))
if num < 0:
    print("Input a positive number")
else:
    for i in range(num):
        print(fibo(i),end=" ")