'''
07. 두 수의 합

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
'''

# 내 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i, num in enumerate(nums):
            num_dic[num] = i
        
        for i, num in enumerate(nums):
            difference = target - num
            if (difference in num_dic) and (i != num_dic[difference]):
                return i, num_dic[difference]

# 모범답안
class Solution:
    def twoSum(self, nums: List[int] , target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 톨합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num] , i]
            nums_map[num] = i