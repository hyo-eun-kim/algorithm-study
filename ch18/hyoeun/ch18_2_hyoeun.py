'''
66. 회전 정렬된 배열 검색 (leetcode 33)
특정 피벗을 기준으로 회전하여 정렬된 배열에서 target값의 인덱스를 출력하라.
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # pivot 위치 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        # print(f"pivot={pivot}")
        # pivot = nums.index(min(nums)) 와 동일한 결과

        left, right = 0, len(nums) - 1  # nums가 정렬되어 있다고 가정한 상태에서의 index라고 보면 된다.
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            # print(f'left={left}, right={right}, mid={mid}, mid_pivot={mid_pivot}')
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = nums.index(min(nums))
        try:
            index = sorted(nums).index(target)
        except:
            return -1
        return index+min_index if index+min_index < len(nums) else index+min_index-len(nums)