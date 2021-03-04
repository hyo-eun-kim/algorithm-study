'''
83. 과반수 엘리먼트

과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

# 내 풀이

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
    # 160 ms