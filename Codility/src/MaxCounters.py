
def solution(N, A):
    counter = [0] * N
    for index in range(len(A)):
        if 1 <= A[index] <= N:
            counter[A[index] - 1] += 1
        if A[index] == N + 1:
            counter = [max(counter)] * N
    return counter