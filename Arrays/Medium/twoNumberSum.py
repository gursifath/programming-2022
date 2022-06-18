def threeNumberSum(array, targetSum):
    array.sort()
    length = len(array)
    tripletSum = []
    for idx in range(length-2):
        left = idx + 1
        right = length - 1
        remainingSum = targetSum - array[idx]

        while(left < right):
            currentSum = array[left] + array[right]
            if currentSum == remainingSum:
                tripletSum.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < remainingSum:
                left += 1
            else:
                right -= 1
    return tripletSum