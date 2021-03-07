# 피보나치수
import collections
class Solution:
    # 가장 기본적인 방법
    # def fib(self, n):
    #     if n <= 1 : 
    #         return n

    #     return self.fib(n-1)+self.fib(n-2)
    dp = collections.defaultdict(int)
    def fib2(self,n):
        if n <=1 :
            return n

        if self.dp[n] :  # 한번 계산한 값을 저장해둠.
            return self.dp[n]
        self.dp[n] = self.fib2(n-1) + self.fib2(n-2)
        return self.dp[n]

        