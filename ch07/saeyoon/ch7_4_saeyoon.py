"""
## 7-4. 배열 파티션

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
"""

def array_pair_sum(nums):
    # 오름차순 정렬하여 짝수번째 인덱스의 값만 더하면 됨
    nums.sort()
    pair_sum = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            pair_sum += num
    return pair_sum


def array_pair_sum2(nums):
    nums.sort()
    return sum(nums[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(array_pair_sum(nums))
    print(array_pair_sum2(nums))