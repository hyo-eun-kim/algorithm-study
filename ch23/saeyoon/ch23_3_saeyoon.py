"""
## 23-3. 계단 오르기

당신은 계단을 오르고 있다. 정상에 도달하기 위해 η 계단을 올라야 한다.
매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라 .
"""
from collections import defaultdict


class Solution:
    def __init__(self):
        self.dp = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(3))