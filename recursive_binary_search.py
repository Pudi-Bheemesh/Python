def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:] ,target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Result: ",result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = recursive_binary_search(numbers,12)
verify(results)
result2 = recursive_binary_search(numbers,6)
verify(result2)