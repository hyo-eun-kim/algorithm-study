'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''
from typing import *
class Solution:
    # 내 풀이 - 104ms (40%)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict.keys():
                mydict[i] += 1
            else:
                mydict[i] = 1

        result = sorted(mydict.items(), key=(lambda x: x[1]), reverse=True)

        return [i[0] for i in result[:k]]