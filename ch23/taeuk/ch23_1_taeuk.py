'''
85. 피보나치 수

피보나치 수를 구하라.

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

'''

class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.dp[n]
    # 28 ms
        
    