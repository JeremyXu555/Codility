A = [1,2,3,4]
# b = []
# p = 0
#
head = A[0]
tail = sum(A[1:])
min = abs(head - tail)

for index in range(1, len(A) - 1):
    head += A[index]
    tail -= A[index]
    if abs(head - tail) < min:
        min = abs(head - tail)

print(min)
