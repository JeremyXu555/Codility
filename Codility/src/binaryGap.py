number = 8899755484651
number_binary = format(number, 'b')

max = 0
count = 0
flag = '1'

for n in number_binary:
    if n == flag and n == '1':
        continue
    elif n == flag and n == '0':
        count += 1
        continue
    elif n != flag and n == '1':
        flag = '1'
        if count > max:
            max = count
        count = 0
        continue
    elif n != flag and n == '0':
        flag = '0'
        count += 1
        continue

print(number_binary)
print(max)


