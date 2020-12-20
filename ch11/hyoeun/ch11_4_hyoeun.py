'''
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''

from typing import *
import collections
import heapq


# 나의 솔루션 (92ms, 18.7MB)
# 104ms(faster than 93%), 18.9MB(less than 41%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_cnt = collections.Counter(nums)
        top_K = [i for i, _ in num_to_cnt.most_common(k)]


# priority queue이용한 solution
# 104ms(faster than 40%), 18.9MB(less than 18%)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        priority_queue = []
        top_K = []
        num_to_cnt = collections.Counter(nums)

        for value, count in num_to_cnt.items():
            # python에서는 작을수록 우선순위가 높기 때문에 - 붙여서 넣어준다
            heapq.heappush(priority_queue, (-count, value))

        # K개의 원소만 pop한다 (빈도가 높은 K개의 원소만 추출해서 list에 담기)
        for i in range(k):
            _, value = heapq.heappop(priority_queue)
            top_K.append(value)
        return top_K

if __name__ == "__main__":
    solution = Solution2()
    solution.topKFrequent([1,1,1,2,2,3], 2)