Python learning Notes:

List Comprehension:

```
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
```

operation before `for` is based on the variable of x, and the list can have its own condition check to filter the elements,
eventually the result comes out is a list.

## Coin Change Problem:

```
def coin_change(target, coins, known_result):
    
    # set up the variable
    min_coin = target
    
    # base case will return and end the function
    if target in coins: 
        known_result[target] = 1
        return 1
    
    # this is where the memorization come into play, avoid the repetive calculation which has been done before.
    elif known_result[target] > 1:
        return known_result[target]
    
    else:
        for i in [c for c in coins if c <= target]:
            coins_need = 1 + coin_change(target - i, coins, known_result)
            
            if coins_need < min_coin:
                min_coin = coins_need
            
            # reset the known_result, every time the target get passed in has been changed
            known_result[target] = min_coin
            
    
    return min_coin
  ```
Test: output should be 8  
```
target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)
coin_change(target, coins, known_results)
```

### Bubble Sort:

```
def buble_sort(arr):
    
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr
```
`range()` contains the starting point but not the ending point
