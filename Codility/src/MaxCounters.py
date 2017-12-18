# a = [ 9, 11, 11, 11, 9, 5, 5, 99, 19, 19, 20, 20, 20, 20, 11]
# print(a[:])
def solution(N, A):
    counter = [0] * N
    for index in range(len(A)):
        if 1 <= A[index] <= N:
            counter[A[index] - 1] += 1
        else:
            counter = [max(counter)] * N
    return counter

# Performance imporovement:
# record the max value and only update the one hasn't been touched