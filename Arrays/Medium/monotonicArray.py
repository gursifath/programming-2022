def isMonotonic(array):
    # 0 for decreasing, 1 for imcreasing
    trend = -1

    for idx in range(len(array)-1):
        if array[idx] > array[idx + 1] and trend != 0:
            if trend != -1:
                return False
            trend = 0
        elif array[idx] < array[idx + 1] and trend != 1:
            if trend != -1:
                return False
            trend = 1
    return True
