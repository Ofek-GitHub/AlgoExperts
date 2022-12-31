

def twoNumberSum(array, targetSum):
    nums = {}
    counter = 0
    for i in range(len(array)):
        nums[array[i]] = (nums.get(array[i], 0) + 1)
    for number in nums:
        counter = targetSum - number
        if counter in nums and counter != number:
            return [counter, number]
    return []


output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(output)
