def selectionSort(array):
    length = len(array)

    for idx in range(length):
        min_idx = idx
        for jdx in range(idx + 1, length):
            if array[jdx] < array[min_idx]:
                min_idx = jdx
        array[idx], array[min_idx] = array[min_idx], array[idx]
    return array
