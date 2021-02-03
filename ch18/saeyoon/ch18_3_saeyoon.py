"""
## 18-3. 두 배열의 교집합

두 배열의 교집합을 구하라.
"""
from typing import *
from bisect import bisect_left


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 36ms
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 48ms
        result = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersection([1, 2, 2, 1], [2, 2]))
    print(sol.intersection2([4, 9, 5], [9, 4, 9, 8, 4]))