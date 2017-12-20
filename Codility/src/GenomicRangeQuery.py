S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]


# container = [0] * len(S)
# result = [0] * len(P)
#
# for s in range(len(S)):
#     if S[s] == 'A':
#         container[s] = 1
#     if S[s] == 'C':
#         container[s] = 2
#     if S[s] == 'G':
#         container[s] = 3
#     if S[s] == 'T':
#         container[s] = 4
#
# for i in range(len(P)):
#     min = 4
#     for j in range(P[i], Q[i] + 1):
#
#         if container[j] < min:
#             min = container[j]
#     result[i] = min


def get_last_seen(S, last_seen, c, idx):
    if S[idx] == c:
        last_seen[idx] = idx
    elif idx > 0:
        last_seen[idx] = last_seen[idx - 1]


def solution(S, P, Q):
    # write your code in Python 3.6
    get_last_seen_A = [-1] * len(S)
    get_last_seen_C = [-1] * len(S)
    get_last_seen_G = [-1] * len(S)
    get_last_seen_T = [-1] * len(S)
    result = [0] * len(Q)

    for idx in range(len(S)):
        get_last_seen(S, get_last_seen_A, 'A', idx)
        get_last_seen(S, get_last_seen_C, 'C', idx)
        get_last_seen(S, get_last_seen_G, 'G', idx)
        get_last_seen(S, get_last_seen_T, 'T', idx)

    for idx in range(len(Q)):
        if get_last_seen_A[Q[idx]] >= P[idx]:
            result[idx] = 1
        elif get_last_seen_C[Q[idx]] >= P[idx]:
            result[idx] = 2
        elif get_last_seen_G[Q[idx]] >= P[idx]:
            result[idx] = 3
        elif get_last_seen_T[Q[idx]] >= P[idx]:
            result[idx] = 4

    return result
# Last seen arrays:
# [-1, 1, 1, 1, 1, 1, 6]
# [0, 0, 0, 3, 4, 4, 4]
# [-1, -1, 2, 2, 2, 2, 2]
# [-1, -1, -1, -1, -1, 5, 5]
# when comparing the index in the second loop, since we are comparing from the smallest 'A' to the biggest
# 'T', so whenever encounter the smaller number, the result[idx] will be assign with the corresponding value
# Array Q holding the last index of the String S, the last_seen array hold the postion of each letter(A,C,G,T)
# has shown at a specific index of the String S
#
# # First operation: last_seen[5] = [1, 4, 2, -1]:
# # when we reach the index of 5 of String S, A was last seen at position of 1, C was last seen at position of 4, etc
# # Since the P[0] = 2, the start of the substring operation is at 2,
# # A hasn't appeared yet, C has was last seen at position of 4 so it must be existed already if the substring start at 2
# # so the first operation C will be the smallest number-letter we will have.
# #
# #