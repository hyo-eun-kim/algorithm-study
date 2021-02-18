"""
## 19-1. 싱글 넘버

딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
"""
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber2(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([4, 1, 2, 1, 2]))
    print(sol.singleNumber2([4, 1, 2, 1, 2]))