def isMonotonic(array):
    if len(array) <= 1:
        return True

    direction = None
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            if direction is None:
                direction = "increasing"
            elif direction == "decreasing":
                return False
        elif array[i] < array[i-1]:
            if direction is None:
                direction = "decreasing"
            elif direction == "increasing":
                return False

    return True


array = [-1, -5, -10, -110, -1100, -1100, -1102, -9000]

res = isMonotonic(array)
print(res)
