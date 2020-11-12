"""
## 7-5. 자신을 제외한 배열의 곱

배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
* 주의: 나눗셈을 하지 않고 O(n)에 풀이하라.
"""

from functools import reduce


def product_except_self(nums):
    def multiply(arr):
        return reduce(lambda x, y: x * y, arr)

    answer = []

    for i in range(len(nums)):
        temp = nums.copy()
        del temp[i]
        answer.append(multiply(temp))

    return answer


def product_except_self2(nums):
    answer = []

    # 왼쪽 곱셈
    left = 1
    for i in range(len(nums)):
        answer.append(left)
        left = left * nums[i]

    # 왼쪽 곱셈에 오른쪽 곱셈 곱함
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] = answer[i] * right
        right = right * nums[i]

    return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))
    print(product_except_self2(nums))