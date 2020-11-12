# https://leetcode.com/problems/two-sum


def my_solution(nums: list, target: int) -> list:
    # 가장 비효율적인 풀이법
    # 문제가 풀리기는 하지만, 좀 더 최적화 할 수 있는 방법을 고민해야 한다.
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i]+nums[j] == target:
                return [i, j]


def solution_3(nums: list, target: int) -> list:
    num_to_index = {}
    # O(n)
    for i, num in enumerate(nums):
        num_to_index[num] = i # key: 값, value: index

    # O(n)
    for i, num in enumerate(nums):
        if target-num in num_to_index and i != num_to_index[target-num]:
            # return [nums_dict[num], nums_dict[target-num]]
            # 라고 하면 nums로 [3, 3]과 같이 같은 값이 들어오는 경우 fail
            # 동일한 key, 다른 value는 저장될 수 없다는 것 기억
            return [i, num_to_index[target-num]]


def solution_4(nums: list, target: int) -> list:
    num_to_index = {}
    for i, num in enumerate(nums):
        if target-num in num_to_index:
            return [num_to_index[target-num], i]
        num_to_index[num] = i


def if_solution(nums: list, target: int) -> list:
    # two-pointer를 이용한 풀이
    # 이러한 풀이는 list가 정렬되어 제공될 때 가능하다.
    # 여기서는 원본 list의 "index"를 반환하여야 하기 때문에 list 정렬 후 다음 풀이를 적용해도 X
    head_index = 0
    tail_index = len(nums)-1
    while tail_index < head_index:
        if nums[head_index]+nums[tail_index] == target:
            return [head_index, tail_index]
        elif nums[head_index]+nums[tail_index] > target:
            # target보다 크다면 tail_index를 왼쪽으로 이동
            head_index -= 1
        else:
            # nums[head_index]+nums[tail_index] < target
            # target보다 작다면 head_index를 오른쪽으로 이동
            tail_index += 1
    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(my_solution(nums, target))
    print(solution_3(nums, target))