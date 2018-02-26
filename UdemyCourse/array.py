# sum pair

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
    # Way of thinking: the first time won't happen anything, only the target truns
    # as the num in the loop which appears at the second time is when the pair been
    #found
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return output
