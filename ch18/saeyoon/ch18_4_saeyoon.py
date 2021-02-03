"""
## 18-4. 두 수의 합 II

정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
* 주의: 배열은 0이 아닌 1부터 시작하는 것으로 한다.
"""
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 64ms
        left, right = 0, len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([2, 3, 4], 6))