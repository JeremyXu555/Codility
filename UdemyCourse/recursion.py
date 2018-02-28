### reverse the string

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        m = int(len(s) / 2)
        ## swap the string left half and right half
        return reverse(s[m:]) + (reverse((s[:m])))

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        # grab the first character of each recursion and put it on the back
        # of the string
        reverse(s[1:]) + s[0]
### Permutation

def permute(s):

    out = []

    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):

            for perm in permute(s[:i] + s[i+1:]):
                ## try to see the way human manually do the permutation, hold one
                ## letter and keep changing the rest of the letters, we are actually
                ## doing the recursion in our brain without notice it
                out += [let + perm]
    return out


### Coin Change Problems:
    ## All the possible combinations

    # Dynamic solution
def coin_change_combination(target, coins):
    combinations = [0] * (target + 1)
    combinations[0] = 1

    for coin in coins:
        amount = 1
        while amount < len(combinations):
            if amount >= coin:
                ## set up the base combinations list with combinations[0] = 1, the iteration variable here
                ## is the dollar amount we are trying to get, we loop through the available coins and adds up
                ## the new possibilities with previous combinations we have already calculated
                combinations[amount] += combinations[amount-coin]

            amount += 1

    return combinations[target]

print(coin_change_combination(12, [1, 2, 5]))

    # Recursion solution
