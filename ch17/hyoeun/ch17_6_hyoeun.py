'''
63. 색 정렬
빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리 정렬을 수행하라.
https://leetcode.com/problems/sort-colors/
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 - red, 1 - white, 2 - blue
        mid_value = 1
        left, cur, right = 0, 0, len(nums)
        while cur < right:
            if nums[cur] < mid_value:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1   # 가장 최근에 위치한 0 다음 위치를 가리키고 있다
                cur += 1    # 계속 이동하는 포인터
            elif nums[cur] == mid_value:
                cur += 1
            else:
                right -= 1
                nums[right], nums[cur] = nums[cur], nums[right]

