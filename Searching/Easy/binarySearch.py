def helper(array, left, right, target):
    if left > right:
        return -1
        
    mid = left + (right-left)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return helper(array, left, mid-1, target)
    else:
        return helper(array, mid+1, right, target)
    

def binarySearch(array, target):
    return helper(array, 0, len(array)-1, target)