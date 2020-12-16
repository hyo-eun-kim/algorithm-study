"""
## 11-4. 상위 K 빈도 요소

k번 이상 등장히는 요소를 추출하라.
"""
from typing import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 124 ms
        if k == len(nums):
            return nums

        return [i for i, _ in Counter(nums).most_common(k)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # 96 ms
        return list(zip(*Counter(nums).most_common(k)))[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
    print(sol.topKFrequent([3,0,1,0], 1)) # [0]
    print(sol.topKFrequent2([1,1,1,2,2,3], 2)) # [1,2]