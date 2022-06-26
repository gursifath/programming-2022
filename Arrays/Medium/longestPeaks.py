def longestPeak(array):
    longestPeak = 0
    for idx in range(1, len(array)-1):
        if array[idx] > array[idx-1] and array[idx] > array[idx+1]:
            currentPeak = 1
            left = idx
            while left > 0 and array[left] > array[left-1]:
                currentPeak += 1
                left -= 1
            while idx < len(array)-1 and array[idx] > array[idx+1]:
                currentPeak += 1
                idx += 1

            if currentPeak > longestPeak:
                longestPeak = currentPeak
    return longestPeak