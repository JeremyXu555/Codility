a = [1, 2, 4, 5]
sum = 0
sum_should = 0
i = 1

while i <= len(a) + 1:
    sum_should += i
    i += 1

for x in a:
    sum += x

b = sum_should - sum

print(b)