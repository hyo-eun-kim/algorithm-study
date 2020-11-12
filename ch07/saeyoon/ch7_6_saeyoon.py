"""
## 7-6. 주식을 사고팔기 가장 좋은 시점

한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
"""


def max_profit(prices):
    if not prices:
        return 0

    profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))