# Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def bss(arr):
    buy = arr[0]
    res = 0
    for i in range(1, len(arr)):
        buy = min(buy, arr[i])
        res = max(res, arr[i] - buy)
    return res

print(bss([78,34,56,12,38]))
print(bss([3,1,4,8]))