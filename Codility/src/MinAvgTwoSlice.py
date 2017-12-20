# https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf

def solution(A):
    # write your code in Python 3.6
    min_val = (A[0] + A[1]) / 2
    min_position = 0

    for index in range(1, len(A) - 2):
        if (A[index] + A[index + 1]) / 2 < min_val:
            min_val = (A[index] + A[index + 1]) / 2
            min_position = index
        if (A[index] + A[index + 1] + A[index + 2]) / 3 < min_val:
            min_val = (A[index] + A[index + 1] + A[index + 2]) / 3
            min_position = index

    if (A[-1] + A[-2]) / 2 < min_val:
        min_val = (A[-1] + A[-2]) / 2
        min_position = len(A) - 2

    return min_position