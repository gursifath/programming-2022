def getNthFib(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return n-1

    a = 0
    b = 1
    for idx in range(n-2):
        nthFibbo = a + b
        a = b
        b = nthFibbo
    return nthFibbo