# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# i-th element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction(buy one and sell one)
# design an algorithm to find the maximum profit.
# note that you cannot sell a stock before you buy.
from typing import List
import sys


# my solution (아래 코드보다 비효율)
def max_profit_1(prices: List[int]) -> int:
    max_profit = 0
    for i, buy_price in enumerate(prices[:-1]):
        sell_price = max(prices[i+1:])  # buy 시점 이후의 가격 중 MAX
        max_profit = max(max_profit, sell_price-buy_price)
    return max_profit


# 저점과 현재 값과의 차이 계산
# 이해하자! 이해하자!
def max_profit_2(prices: List[int]) -> int:
    max_profit = 0  # max_profit = -sys.maxsize
    buy_price = sys.maxsize

    for price in prices:
        buy_price = min(price, buy_price)
        max_profit = max(max_profit, price-buy_price)
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_1(prices))
    print(max_profit_2(prices))