def minimumWaitingTime(queries):
    queries.sort()
    runningSum = 0
    finalSum = 0

    for idx in range(len(queries)-1):
        runningSum += queries[idx]
        finalSum += runningSum

    # for query in queries:
    #     finalSum += runningSum
    #     runningSum += query
    return finalSum