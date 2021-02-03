"""
## 18-2. 회전 정렬된 배열 검색

특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.
"""
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                if nums[mid] < nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if target < nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return mid

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))