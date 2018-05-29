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

    # this is where the memorization come into play, avoid the repetitive calculation which has been done before.
    elif known_result[target] > 1:
        return known_result[target]

    else:
        for i in [c for c in coins if c <= target]:
            // Let's imagine when the function has return 1 from the base case, if we don't have the plus one, // the coins_need will be always one, so the plus one will be use for accumulate the coins need so // far 
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

### Selection Sort:
Sorting from the right
```

def select_sort(arr):
    for fillslot in range(len(arr)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp

    return arr    
```
Sorting from the left:

```
def select_sort(arr):

    # For every slot in array
    for fillslot in range(len(arr)):
        positionOfMin=fillslot

        # For every set of 0 to fillslot+1
        for location in range(fillslot+1, len(arr)):

            # Set minum's location
            if arr[location]<arr[positionOfMin]:
                positionOfMin = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMin]
        arr[positionOfMin] = temp
    return arr

```
2018 May 29
```
pointer = 0

for x in range(0, len(arr)):
    minVal = arr[x]
    for y in range(pointer, len(arr)):
        if arr[y] < minVal:
            temp = arr[y]
            arr[y] = arr[pointer]
            arr[pointer] = temp
    pointer += 1

```



### Insert Sort

```

def insert_sort(arr):

    for i in range(1, len(arr)):

        # define the position and currentValue for comparasion
        position = i
        currentValue = arr[position]

        while position > 0 and arr[position-1] > currentValue:
            # the position is keeping changing, but the currentValue will be always as the mark for comparing
            # whenever the value before the position is bigger than currentValue, the current position value will be
            # set as the bigger value
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = currentValue

    return arr

```


### Merge Sort

```
def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1

            k += 1
        # while the programme executing here one half must has been exhausted, so either side executed first won't matter and
        # it will be only executed once to collected the last element which is the biggest number
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr

```
