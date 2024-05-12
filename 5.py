def recur_factorial(n):
    if n == 1:
        return 1
    else:
        final = n * recur_factorial(n - 1)
        return final

a = int(input("Enter your number: "))
print(recur_factorial(a))
