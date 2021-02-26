# 주식을 사고팔기 가장 좋은 시점
# 여러번의 거래로 낼수 있는 최대 이익을 산출하라
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit += prices[i+1]-prices[i]
        return profit