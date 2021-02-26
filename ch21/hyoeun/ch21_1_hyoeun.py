'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
'''

# Runtime: 40 ms, faster than 91.15% of Python online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 14.4 MB, less than 87.71% of Python online submissions for Best Time to Buy and Sell Stock II.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        total_profit = 0
        before_price = prices[0]  # before price
        lmin_price = prices[0]  # local minimum price

        for cur_price in prices:
            if before_price > cur_price:
                # 다음의 price가 이전 대비 낮아지는 경우 팔아버린다!
                total_profit += (before_price - lmin_price)
                # update local minimum price
                lmin_price = cur_price
            if lmin_price > cur_price:
                # update local minimum price
                lmin_price = cur_price
            before_price = cur_price

        total_profit += (cur_price - lmin_price)
        return total_profit