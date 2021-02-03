'''
68. 두 수의 합 2 (leetcode 167)
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를
이 문제에서 배열의 index가 0이 아닌 1부터 시작하는 것으로 간주
동일한 element를 사용하면 안 되고, 정답은 오로지 1개만 존재한다고 가정하라.
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
from typing import List

# Runtime: 80 ms, faster than 22.92% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.8 MB, less than 5.47% of Python3 online submissions for Two Sum II - Input array is sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            sum_val = numbers[left] + numbers[right]
            if sum_val < target:
                # target보다 작은 경우
                left += 1
            else:
                # target보다 큰 경우
                right -= 1
        return [left + 1, right + 1]