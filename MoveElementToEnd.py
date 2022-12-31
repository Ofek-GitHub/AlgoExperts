def moveElementToEnd(array, toMove):
    listToMove = []
    pointerOne = 0
    length = len(array)
    while pointerOne < length:
        if array[pointerOne] == toMove:
            listToMove.append(array[pointerOne])
            array.pop(pointerOne)
            length = len(array)
        else:
            pointerOne += 1

    array = array + listToMove
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
toMove = 2
res = moveElementToEnd(array, toMove)
print(res)
