# O(nlogn) time
# O(n) space
def mergeOverlappingIntervals(intervals):
    mergedIntervals = []
    intervals.sort()
    currentInterval = intervals[0]
    idx = 1
    while idx < len(intervals):
        if currentInterval[1] >= intervals[idx][0]:
            currentInterval[1] = max(intervals[idx][1], currentInterval[1])
        else:
            mergedIntervals.append(currentInterval)
            currentInterval = intervals[idx]
        idx += 1
    mergedIntervals.append(currentInterval)
    return mergedIntervals