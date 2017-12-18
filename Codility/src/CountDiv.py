# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    counter = 0
    X = list(range(A, B + 1))
    for x in X:
        if x % K == 0:
            counter += 1
    return counter