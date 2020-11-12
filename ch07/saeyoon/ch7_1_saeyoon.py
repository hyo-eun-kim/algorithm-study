"""
## 7-1. 두 수의 합

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum2(nums, target):
    # target에서 원소를 뺀 값이 리스트 내에 존재하는지 탐색
    for i, num in enumerate(nums):
        c = target - num

        if c in nums[i+1:]:
            return [nums.index(num), nums[i+1:].index(c) + (i+1)]


def two_sum3(nums, target):
    nums_dict = {}
    # 키, 값을 바꾸어 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_dict[num] = i

    # 타겟에서 첫 번째 수를 뺀 값을 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_dict and i != nums_dict[target - num]:
            return [nums.index(num), nums_dict[target - num]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
