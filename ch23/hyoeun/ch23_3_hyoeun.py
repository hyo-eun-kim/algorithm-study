'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

from collections import defaultdict

class Solution:
    dp = defaultdict(int)
    dp[1] = 1
    dp[2] = 2

    def climbStairs(self, n):
        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]