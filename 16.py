arr = [1,2,3,4,5,3,2]
l = 0

key = 5
r = len(arr) - 1
for i in range(0,len(arr)//2):
    mid = len(arr)//2
    if (key==mid):
        print(i)
    elif (key < mid):
        r = mid-1
    else:
        r = mid +1
