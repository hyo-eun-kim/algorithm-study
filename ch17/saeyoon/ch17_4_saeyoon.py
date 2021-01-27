"""
## 17-4. 가장 큰 수

항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.
"""
from typing import *
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 40ms
        nums = list(map(str, nums))
        nums.sort(key = cmp_to_key(lambda x, y: ((x+y)<(y+x)) - ((x+y)>(y+x))))
        return ''.join(nums).lstrip('0') or '0'


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3, 30, 34, 5, 9]))
    print(sol.largestNumber([0, 0]))