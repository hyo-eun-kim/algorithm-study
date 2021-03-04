'''
87. 계단 오르기

당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다. 매번 각각 1계단 또는 2계단씩 오를 수 있다면 
정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라.

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

# 메모이제이션
class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.dp[n]
    # 28 ms
    
# 더 간단히 표현
class Solution:
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    # 24 ms