'''
136. Single Number
https://leetcode.com/problems/single-number/
하나만 존재하는 element를 찾아라.
'''
from collections import defaultdict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        ans = [i for i, j in count.items() if j == 1]
        return ans[0]


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:

        nums.sort()
        prev = None
        for i, num in enumerate(nums[:-1]):
            if num != prev and num != nums[i + 1]:
                return num
            prev = num
        return nums[-1]

# 책 답지 .. 오오 !
# x xor x = 0 이라는 것을 이용한 아이디어!
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result