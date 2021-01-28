"""
## 17-6. 색 정렬

빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리 정렬을 수행하라.
"""
from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 28ms
        i = j = k = 0
        for num in nums:
            if num == 0:
                i += 1
            elif num == 1:
                j += 1
            else:
                k += 1

        nums[:i] = [0] * i
        nums[i:i+j] = [1] * j
        nums[i+j:] = [2] * k

    def sortColors2(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums)
        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)