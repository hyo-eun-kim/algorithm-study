'''
61. 가장 큰 수
항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.
https://leetcode.com/problems/largest-number/
'''
from typing import List

# 73과 7을 비교할 때
# "73"+"7"="737", "7"+"73"="773"을 비교하면 된다는 것!

# merge sort 이용한 풀이
class Solution:
    @staticmethod
    def compare(num1, num2):
        if str(num1) + str(num2) > str(num2) + str(num1):
            return True
        else:
            return False

    def merge(self, l1, l2):
        l1_index = 0
        l2_index = 0
        sorted_list = []
        while l1_index != len(l1) and l2_index != len(l2):
            if Solution.compare(l1[l1_index], l2[l2_index]):
                sorted_list.append(l1[l1_index])
                l1_index += 1
            else:
                sorted_list.append(l2[l2_index])
                l2_index += 1

        if l1_index != len(l1):
            sorted_list.extend(l1[l1_index:])
        else:
            sorted_list.extend(l2[l2_index:])
        return sorted_list

    def divide(self, nums: List[int]):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        left = self.divide(nums[:mid])
        right = self.divide(nums[mid:])
        return self.merge(left, right)

    def largestNumber(self, nums: List[int]) -> str:
        ret = self.divide(nums)
        ret = ''.join(list(map(str, ret)))
        if int(ret) == 0:
            return "0"
        return ret
