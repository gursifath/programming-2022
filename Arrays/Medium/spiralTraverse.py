def spiralTraverse(array):
    num_rows = len(array)
    num_cols = len(array[0])
    row_start = 0
    row_end = num_rows - 1
    col_start = 0
    col_end = num_cols - 1
    spiralArray = []

    while row_start <= row_end and col_start <= col_end:
        for idx in range(col_start, col_end + 1):
            spiralArray.append(array[row_start][idx])
        row_start += 1

        for idx in range(row_start, row_end + 1):
            spiralArray.append(array[idx][col_end])
        col_end -= 1

        if row_start <= row_end:
            for idx in range(col_end, col_start - 1, -1):
                spiralArray.append(array[row_end][idx])
            row_end -= 1

        if col_start <= col_end:
            for idx in range(row_end, row_start - 1, -1):
                spiralArray.append(array[idx][col_start])
            col_start += 1
        
    return spiralArray
