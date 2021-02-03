'''
65. 이진검색 (leetcode 704)
정렬된 nums를 받아 이진검색으로 target에 해당하는 인덱스를 찾아라.
https://leetcode.com/problems/binary-search/
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, value, low, high):
            if (low > high):
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, value, low, mid - 1)
            else:
                return binary_search(nums, value, mid + 1, high)

        return binary_search(nums, target, 0, len(nums) - 1)
