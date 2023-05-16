def insertionSortRec(A, start, end):
    value = A[start]
    loc = start
    while loc > 0 and A[loc - 1] > value:
        A[loc] = A[loc - 1]
        loc -= 1
    A[loc] = value

    if start + 1 < end:
        insertionSortRec(A, start + 1, end)
