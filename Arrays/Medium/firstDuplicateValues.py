def firstDuplicateValue(array):
    for idx in range(len(array)):
        if array[abs(array[idx])-1] < 0:
            return abs(array[idx])
        array[abs(array[idx])-1] *= -1

    return -1
        