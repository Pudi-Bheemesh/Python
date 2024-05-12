a = int(input())
if a <= 0:
    print("Enter a positive Number")
else:
    for i in range(1,a):
        if a % i == 0:
            if i % 2 != 0:
                print(i)
