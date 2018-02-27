### sum pair

def sum_pair(arr, k):

    # edge check
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num
    # put the visited num into the seen set, and if the target has been already
    # inside of the seen set, we have found the pair matching.
    # Way of thinking: the first time won't happen anything, only the target turns
    # as the num in the loop which appears at the second time is when the pair been
    #found
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return output

### Reverse word

def rev_word(s):

    space = [' ']
    length = len(s)
    output = []
    i = 0

    while i < length:

        if s[i] not in space:

            startIndex = i

            while s[i] not in space and i < length:
                i += 1

            ## the syntax of array[startIndex, endIndex], the startIndex will be
            ## included while the endIndex will not
            word = s[startIndex : i]

            output.append(word)

        i += 1

    return list(reversed(output))

### Max Continuous Sum

def continuous_sum(arr):

    current_sum = arr[0]
    max_sum = current_sum

    i = 1

    while i < len(arr):

        # if the current_sum is smaller than the current number in the array
        # that means the value has been accumulated so far is less than the current
        # number, so we need to start a new current_max round
       current_sum = max(current_sum+arr[i], arr[i])

       max_sum = max(current_sum, max_sum)

       i += 1

    return max_sum

### String Compression
def str_compression(s):

    i = 1
    count = 1
    output = ''

    ## Edge Check
    if len(s) == 1:
        output = s + str(1)

    if len(s) == 0:
        return ''

    while i < len(s):

        if s[i-1] == s[i]:
            count += 1
        else:
            output += s[i-1]
            output += str(count)
            count = 1

        i += 1

### anagram Check
def anagram(s1, s2):

    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    if len(s1) != len(s2):
        return False

    counter = {}
    ## make a dictionary for recording the occurences of the character

    for c in s1:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for c in s2:
        counter[c] -= 1
                
    for c in counter:
        if counter[c] != 0:
            return False


    return True
