A = [1, 2, 3, 4, 5, 6]
# A.sort()
#
# for index in range(0, len(A) - 1):
#     if A[index] + 1 != A[index+1]:
#         c = 0
#         break
#     else:
#         c = 1

def solution(A):
    counter = [0] * len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else:
            if counter[element - 1] != 0:
                return 0
            counter[element - 1] = 1

    return 1

