import collections
a = [ 9, 11, 11, 11, 9, 5, 5, 99, 19, 19, 20, 20, 20, 20, 11]

a.sort()
i = 0
print(a)
while i + 1 < len(a):
    print(i)
    if a[i] != a[i+1]:
        if a[i-1] != a[i]:
            b = a[i]
        else:
            b = a[i+1]
        break
    i += 2
try: b
except NameError: b = None

if b is None:
    b = a[len(a)-1]

print(b)

# for x in a:
#     if x not in seen:
#         uniq.append(x)
#         seen.add(x)
# print(seen)

# i = 0
# mark = 0
# duplicate = False
# duplicateCount = 0
#
# while i < len(a):
#     j = i + 1
#     while j < len(a):
#         print('while loop')
#         print(a)
#         print(f"i:{i}")
#         print(f"j:{j}")
#         print('while loop')
#
#         if a[i] == a[j]:
#             print('if find the same value: ')
#             print(f"i:{i}")
#             print(f"j:{j}")
#             duplicate = True
#             del a[j]
#             if i == len(a) - 1 or i == 0 or j == len(a) - 1:
#                 del a[i]
#             print(a)
#             j += 1
#         if j == len(a) - 1 and duplicate:
#             print('when j reach the last index and duplicate: ')
#             print(f"i:{i}")
#             print(f"j:{j}")
#             duplicate = False
#             print('duplicate')
#             del a[i]
#             i -= 1
#             print(a)
#         else:
#             j += 1
#     i += 1
#
# print(f"Final Result: {a}")

