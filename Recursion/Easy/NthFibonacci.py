def getNthFib(n):
    if n == 1 or n == 2:
        return n-1

    return getNthFib(n-1) + getNthFib(n-2)
