Python learning Notes:

List Comprehension:

```
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
```

operation before `for` is based on the variable of x, and the list can have its own condition check to filter the elements,
eventually the result comes out is a list.
