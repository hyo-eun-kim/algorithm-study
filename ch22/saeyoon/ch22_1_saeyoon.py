"""
## 22-1. 과반수 엘리먼트

과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라
"""
from typing import *
from collections import Counter
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 160ms
        return Counter(nums).most_common(1)[0][0]

    def majorityElement2(self, nums: List[int]) -> int:
        # 244ms
        if len(nums) == 1:
            return nums[0]
        half = len(nums) // 2
        a = self.majorityElement2(nums[:half])
        b = self.majorityElement2(nums[half:])
        return [b, a][nums.count(a) > half]

    def majorityElement3(self, nums: List[int]) -> int:
        # 172ms
        counts = defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(sol.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
    print(sol.majorityElement3([2, 2, 1, 1, 1, 2, 2]))