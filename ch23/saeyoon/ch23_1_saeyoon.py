"""
## 23-1. 피보나치 수

피보나치 수를 구하라.
"""
from collections import defaultdict


class Solution:
    # 하향식 풀이 - 메모이제이션
    def __init__(self):
        self.dp = defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


class Solution2:
    # 상향식 풀이 - 타뷸레이션
    def __init__(self):
        self.dp = defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(3))

    sol2 = Solution2()
    print(sol2.fib(3))