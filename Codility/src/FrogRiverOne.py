X = 6
A = [1,2,3,5,6,6,7,5]
c = 0

if X not in A:
    c = -1
for index in range(0, len(A)):
    if A[index] == X:
        c = index
        # split the Array into two separate parts
        left = A[0:index + 1]
        right = A[index+1: len(A)]
        for x in range(1, X):
            if x not in left:
                c = -1
                if X not in right:
                    # this case is which the X is the last one showing up, but not all the postion
                    # has been covered
                    c = -1
                    print('can not be reached')
                break
            # this means all the position has been covered:
            if x == X - 1:
                print(c)
                print('find the right index')



# def solution(X, A):
#     if X not in A:
#         return -1
#     for index in range(0, len(A)):
#         if A[index] == X:
#             # split the Array into two separate parts
#             left = A[0:index + 1]
#             right = A[index+1: len(A)]
#             for x in range(1, X):
#                 if x not in left:
#                     if X not in right:
#                     # this case is which the X is the last one showing up, but not all the postion
#                     # has been covered
#                         return -1
#                     break
#             # this means all the position has been covered:
#                 if x == X - 1:
#                     return index