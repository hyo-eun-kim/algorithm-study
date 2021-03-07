# 최대 서브 배열
# 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라

class Solution:
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])  # 앞에서 부터 값을 계산하면서 누적합을 계산한다.
        return max(nums)

        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        
        # for i in range(1,n):
        #     dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        # return max(dp)