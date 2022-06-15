def insertionSort(array):
    length = len(array)
    # swap elements at every step
    for idx in range(1, length):
        jdx = idx
        while(jdx > 0 and array[jdx] < array[jdx-1]):
            array[jdx], array[jdx-1] = array[jdx-1], array[jdx]
            jdx -= 1 
    return array