'''
86. 최대 서브 배열

합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-100000]
Output: -100000

'''

# 내 풀이
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            else:
                nums[i] += 0
            print(nums)
        return max(nums)
    # 64 ms