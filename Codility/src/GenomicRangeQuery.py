S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]


container = [0] * len(S)
result = [0] * len(P)

for s in range(len(S)):
    if S[s] == 'A':
        container[s] = 1
    if S[s] == 'C':
        container[s] = 2
    if S[s] == 'G':
        container[s] = 3
    if S[s] == 'T':
        container[s] = 4

for i in range(len(P)):
    min = 4
    for j in range(P[i], Q[i] + 1):

        if container[j] < min:
            min = container[j]
    result[i] = min

print(result)