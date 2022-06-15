def findThreeLargestNumbers(array):

    largestNums = [float('-inf'), float('-inf'), float('-inf')]
    for element in array:
        if element > largestNums[2]:
            largestNums[0] = largestNums[1]
            largestNums[1] = largestNums[2]
            largestNums[2] = element
        elif element > largestNums[1]:
            largestNums[0] = largestNums[1]
            largestNums[1] = element
        elif element > largestNums[0]:
            largestNums[0] = element
    return largestNums
            
        
