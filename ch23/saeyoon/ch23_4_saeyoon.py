"""
## 23-4. 집 도둑

당신은 전문털이범이다.
어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 기능하다.
각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어있다.
훔칠 수 있는 가장 큰 금액을 출력하라.
"""
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([2, 7, 9, 3, 1]))