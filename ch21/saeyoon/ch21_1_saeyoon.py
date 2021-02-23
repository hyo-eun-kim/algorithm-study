"""
## 21-1. 주식을 사고팔기 가장 좋은 시점 II

여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
"""
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 68ms
        return sum((prices[i] - prices[i-1]) for i in range(1, len(prices)) if prices[i] > prices[i-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))