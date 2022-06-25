def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    ptr1 = ptr2 = 0
    minDiff = float("inf")
    currDiff = 0

    while ptr1 < len(arrayOne) and ptr2 < len(arrayTwo):
        currDiff = abs(arrayOne[ptr1] - arrayTwo[ptr2])
        if currDiff < minDiff:
            minDiff = currDiff
            minDiffPair = (arrayOne[ptr1], arrayTwo[ptr2])

        if arrayOne[ptr1] < arrayTwo[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1

    return minDiffPair