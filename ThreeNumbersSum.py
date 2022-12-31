

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

res = threeNumberSum(array, targetSum)
print(res)
