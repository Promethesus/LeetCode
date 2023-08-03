


def max_profit(prices:list[int])-> int:
    l,r = 0, 1
    max_value = 0
    while l < r and r < len(prices):
        max_value = max(max_value, (prices[r]- prices[l]))
        if prices[r] < prices[l]:
            l = r
            r +=1
        else:
            r+=1
    return max_value



print(max_profit(prices = [7,1,5,3,6,4]))