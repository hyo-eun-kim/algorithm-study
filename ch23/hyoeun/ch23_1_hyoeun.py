'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/submissions/
'''

# Runtime: 948 ms
# Memory Usage: 14.2 MB
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)


# 위보다 효율적
# 하향식!
# Runtime: 24 ms, faster than 95.83% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.2 MB, less than 73.58% of Python3 online submissions for Fibonacci Number.
class Solution:
    dp = defaultdict(int)
    dp[0] = 0
    dp[1] = 1

    def fib(self, n: int) -> int:
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.dp[n - 1] + self.dp[n - 2]
        return self.dp[n]

# 상향식!
# Runtime: 20 ms, faster than 99.15% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.3 MB, less than 9.96% of Python3 online submissions for Fibonacci Number.
class Solution:
    dp = defaultdict(int)
    dp[0] = 0
    dp[1] = 1

    def fib(self, n: int) -> int:
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]