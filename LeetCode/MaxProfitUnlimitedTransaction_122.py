def unlimit_transaction(price):

    valley = price[0]
    peak = price[0]
    i = 0
    max_profit = 0

    while i < len(price) - 1:

        while i < len(price) - 1 and price[i] > price[i + 1]:
            i += 1
        valley = price[i]
        # basic principle: once the price grows up, the valley loop will be ended
        print('valley', valley)

        while i < len(price) - 1 and price[i] < price[i + 1]:
            i += 1
        peak = price[i]

        # As the i keeps adding up, the valley and peak are holding the value
        # of two ends in a continuous phase, which will make more sense in the next
        # solution
        print('peak', peak)

        max_profit += (peak - valley)


    return max_profit

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

def unlimit_transaction2(price):

    max_profit = 0

    while i < len(price) - 1:
        if price[i] < price[i + 1]:
            max_profit += price[i + 1] - price[i]

        i += 1

    return max_profit
