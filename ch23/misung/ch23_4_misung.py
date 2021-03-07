# 집도둑
# 당신은 전문털이범이다. 어느 집에서든 돈을 훔쳐올수 있지만,
# 경보 시스템 때문에 바로 옆집은 훔칠수 없고
# 한 칸 이상 떨어진 집만 가능하다.
# 각 집에는 훔칠수 있는 돈의 액수가 입력값으로 표기되어있다.
# 훔칠수 있는 가장 큰 금액을 출력하라

class Solution:
    def rob(self, nums):
            if not nums: # nums가 없으면 0 리턴
                return 0
            
            if len(nums) <= 2:  # nums 가 2개 이하면 더 큰숫자 리턴
                return max(nums)

            dp = [0] * len(nums) # dp = [0,0,0,... 0 ]
            dp[0] = nums[0]      # dp = [nums[0], 0,0,0...0]
            dp[1] = max(nums[0], nums[1])  # 더 큰거를 dp[1] 에 넣어줌

            for house in range(2,len(nums)): 
                dp[house] = max(dp[house -1], nums[house] + dp [house -2]) # 한집 건넛집까지의 최대값과, 현재집의 숫자값과의 합을 비교
                
            return dp[-1] 