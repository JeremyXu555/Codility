### reverse the string

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        m = int(len(s) / 2)
        ## swap the string left half and right half
        return reverse(s[m:]) + (reverse((s[:m])))

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
