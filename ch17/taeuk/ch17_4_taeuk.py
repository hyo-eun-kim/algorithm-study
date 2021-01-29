'''
61. 가장 큰 수

항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
'''

# 내 풀이
import functools
class Solution(object):
    def largestNumber(self, nums: List[int]) -> str:
        r = ''.join(sorted(map(str, nums), key = functools.cmp_to_key(lambda x, y: -1 if x + y > y + x else 1)))
        return r.lstrip('0') or '0'
    # 36 ms