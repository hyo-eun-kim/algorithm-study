"""
## 7-2. 빗물 트래핑

높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
"""
from itertools import combinations


def three_sum(nums):
    nums.sort()
    com = combinations(nums, 3)
    answer = []
    for i in com:
        if sum(i) == 0 and list(i) not in answer:
            answer.append(list(i))
    return answer


def three_sum2(nums):
    # 투 포인터를 이용한 풀이
    answer = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i+1, len(nums)-1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                answer.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return answer


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
    print(three_sum2(nums))