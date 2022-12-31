def isValidSubsequence(array, sequence):
    if len(array) < len(sequence):
        return False

    counter = 0
    for i in range(len(array)):
        if counter >= len(sequence):
            break
        if int(array[i]) == int(sequence[counter]):
            counter += 1

    if counter == len(sequence):
        return True
    else:
        return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]

res = isValidSubsequence(array, sequence)
print(res)
