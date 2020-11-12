# https://leetcode.com/problems/3sum/
# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.
from typing import List

# 나의 풀이
def solution_1(nums: List[int]) -> List[List[int]]:
    nums.sort()
    num_to_idx = {}
    for i, num in enumerate(nums):
        num_to_idx[num] = i

    # result = []
    result = set() # set 사용하니 time exceeded 문제 해결!
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            find_value = -(nums[i]+nums[j])
            if find_value in num_to_idx and num_to_idx[find_value] > j:
                # result.append([nums[i], nums[j], find_values])
                result.add((nums[i], nums[j], find_value))
    return list(result)


# https://leetcode.com/problems/3sum/discuss/404887/Python3-solution-extend-from-sum-2
# two pointer 이용한 풀이 (추천)
def solution_2(nums: List[int]) -> List[List[int]]:
    nums.sort() # 정렬
    result = set()

    for i in range(len(nums)-2):
        left_ptr = i+1
        right_ptr = len(nums)-1
        while left_ptr < right_ptr:
            sum_val = nums[i]+nums[left_ptr]+nums[right_ptr]
            if sum_val == 0:
                result.add((nums[i], nums[left_ptr], nums[right_ptr]))
                left_ptr += 1
                right_ptr -= 1
            elif sum_val < 0:
                left_ptr += 1
            else:
                right_ptr -= 1
    return list(result)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution_1(nums))
    print(solution_2(nums))
