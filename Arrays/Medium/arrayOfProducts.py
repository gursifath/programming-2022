def arrayOfProducts(array):

    output = [1]*len(array)
    leftRunningProduct = rightRunningProduct = 1
    for idx in range(len(array)):
        output[idx] = leftRunningProduct
        leftRunningProduct *= array[idx]

    for idx in range(len(array)-1, -1, -1):
        output[idx] *= rightRunningProduct
        rightRunningProduct *= array[idx]

    return output
    