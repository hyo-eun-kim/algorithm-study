# https://leetcode.com/problems/array-partition-i/
# given an integer array nums of 2n integers,
# group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized.
# return the maximized sum.
from typing import List


def solution_1(nums: List[int]) -> int:
    # 1. 정렬
    nums.sort()
    # 2. 홀수번째 값의 합(짝수 index)
    return sum(nums[::2])


if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print(solution_1(nums))
