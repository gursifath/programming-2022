# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def helper(array, depth):
    finalSum = 0
    for element in array:
        if type(element) is list:
            finalSum += helper(element, depth+1)
        else:
            finalSum += element
    return finalSum*depth
    
def productSum(array):
    return helper(array, 1)