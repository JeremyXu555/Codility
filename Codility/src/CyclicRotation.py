A = [3, 8, 9, 7, 6]
B = [0] * len(A)
K = 2
i = 0
while i < len(A):
    j = (i + K) % len(A)
    B[j] = A[i]
    i += 1
