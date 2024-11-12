"""
    This program will gain the maximum profit,
    maximum - minimum price
"""

def max_profit(prices):
    """
    maximum for sell
    minimum for buy
    """
    maximum_price = 0
    for days in range(len(prices)): #PyLint wants me to code with enumerate but the code will run an error
        for mini in range(days, len(prices)):
            count = prices[mini] - prices[days]
            if count > maximum_price:
                maximum_price = count
    return maximum_price
user_enter_stock = input("Please enter number to calculate stock from Day 0 to Day 7: ")
user_enter_stock = list(map(int, user_enter_stock.split()))
gain_profit = max_profit(user_enter_stock)
print(gain_profit)
