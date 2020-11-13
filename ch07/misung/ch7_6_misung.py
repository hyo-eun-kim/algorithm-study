# 주식을 사고팔기 가장 좋은 시점
# 한번의 거래로 낼수 있는 최대 이익을 산출하라

import sys

prices = [7,1,5,3,6,4]

def maxProfit(prices): 
    
    min_price = sys.maxsize
    profit = 0

    for i in prices:
        min_price = min(min_price, i)
        profit = max(profit, i- min_price)
    return profit 
    
maxProfit(prices)
