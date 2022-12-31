def evenSumIndex(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
    for i in range(len(arr)):
        sum2 += arr[i]
        if sum2 == sum1/2:
            return i
    return False


array = [2, 13, 4, 7, 9, 5, 6, 24]

res = evenSumIndex(array)
print(res)
