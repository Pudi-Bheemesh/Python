t = int(input())
i = 0
balance = 0
while i<t:
    c = input("Enter 'D' for deposit and 'W' for withdrawal: ")
    n = int(input("Enter amount: "))
    if c == 'D' or c == 'd':
        balance = balance + n
    elif c == 'W' or c == 'w':
        balance = balance - n
    else:
        print("Invalid character")
    i += 1

print(balance)