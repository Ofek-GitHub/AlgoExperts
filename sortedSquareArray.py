def sortedSquaredArray(array):
    # Initialize two pointers at the beginning and end of the list
    left = 0
    right = len(array) - 1

    # Initialize an empty result list
    result = []

    # Move the pointers towards each other until they meet
    while left <= right:
        # If the element at the left pointer is larger, add it to the result list
        # and move the left pointer one position to the right
        if abs(array[left]) > abs(array[right]):
            result.append(array[left] ** 2)
            left += 1
        # If the element at the right pointer is larger, add it to the result list
        # and move the right pointer one position to the left
        else:
            result.append(array[right] ** 2)
            right -= 1

    # Return the result list in reverse order, since we added the elements in
    # descending order
    return result[::-1]
