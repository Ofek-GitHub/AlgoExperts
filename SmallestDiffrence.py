def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    j = 0
    i = 0
    pointerOne = arrayOne[0]
    pointerTwo = arrayTwo[0]
    res = abs(pointerOne - pointerTwo)
    answer = [pointerOne, pointerTwo]

    while i < len(arrayOne) and j < len(arrayTwo):
        pointerOne = arrayOne[i]
        pointerTwo = arrayTwo[j]
        temp = abs(pointerOne - pointerTwo)
        if temp < res:
            res = temp
            answer = [pointerOne, pointerTwo]
        if pointerOne < pointerTwo:
            i += 1
        elif pointerOne > pointerTwo:
            j += 1
        else:
            return [pointerOne, pointerTwo]
    return answer


arrayOne = [10, 0, 20, 25]
arrayTwo = [1005, 1006, 1014, 1032, 1031]
res = smallestDifference(arrayOne, arrayTwo)
print(res)
