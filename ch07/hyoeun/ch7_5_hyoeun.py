# https://leetcode.com/problems/product-of-array-except-self/
# given an array nums of n integers where n>1
# return an array output such that output[i] is equal to
# the product of all the elements of nums except nums[i]
# please solve it without division and in O(n)
from typing import List


# 왜 이걸 생각하지 못했을까..
def solution_1(nums: List[int])->List[int]:
    # i index의 왼쪽에 위치한 모든 값의 곱
    left_product = []
    product = 1
    for value in nums:
        left_product.append(product)
        product *= value

    # i index의 오른쪽에 위치한 모든 값의 곱
    right_product = []
    product = 1
    for value in nums[::-1]:
        right_product.insert(0, product)
        product *= value

    result = []
    for i in range(len(nums)):
        # i index의 왼쪽에 위치한 모든 값의 곱 * 오른쪽에 위치한 모든 값의 곱
        result.append(left_product[i]*right_product[i])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(solution_1(nums))