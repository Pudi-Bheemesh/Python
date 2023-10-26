import random
a = random.randrange(0,9) + 10*random.randrange(0,9) +100*random.randrange(0,9) + 1000*random.randrange(0,9)
print("Your OTP is:", +a)
print("\n\n")
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


for row in picture:
    for image in row:
        if image == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')