def maxProfit(arr):
    j = 1
    profit_arr = []
    # convert the stock price to the array store the profilt for each day
    while j < len(arr):
        profit_arr.append(arr[j] - arr[j-1])
        j += 1

    # Turn the problem to get the max value of continuous elements
    max_sum = current_sum = profit_arr[0]
    i = 1

    while i < len(profit_arr):
        current_sum = max(current_sum + profit_arr[i], profit_arr[i])
        max_sum = max(current_sum, max_sum)
        i += 1

    return max_sum

def maxProfit2(price):
    # create a list to store the lowest price so far
    # Create another list to store the max profit so far

    lowest_price = [0] * len(price)
    max_profit = [0] * len(price)
    i = 1

    while i < len(price):

        lowest_price[i] = min(lowest_price[i-1], price[i])

        # compare the profit of previous wiht the value of selling the
        # price at this moment
        max_profit[i] = max(max_profit[i-1], price[i] - lowest_price[i])
        i += 1

    return max_profit[-1]
