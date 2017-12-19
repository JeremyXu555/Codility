def solution(A):
    # write your code in Python 3.6
    zero_count = 0
    pairs_count = 0
    for a in A:

        if a == 0:
            zero_count += 1
        else:
            pairs_count += zero_count
            if pairs_count > 1000000000:
                return -1
    return pairs_count