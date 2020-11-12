'''
12. 주식을 사고팔기 가장 좋은 시점

한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
'''

# 내 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices가 []일 경우 에러가 발생
        if not prices:
            return 0
        
        min_price = max(prices)
        max_profit = 0
        # 앞에서부터 뒤로 이동해가며 최솟값, 최댓값을 갱신한다.
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit, price - min_price) 
        
        return max_profit

# 모범답안
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize
    
    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit