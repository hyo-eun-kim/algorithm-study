'''
59. 구간 병합
겹치는 구간을 병합하라.
https://leetcode.com/problems/merge-intervals/
'''

import heapq
from typing import List

# my solution
# Runtime: 136 ms, faster than 7.04%
# Memory Usage: 16.1 MB, less than 85.04%
# heapq 굳이 사용할 필요 X .... 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        for interval in intervals:
            heapq.heappush(heap, interval)

        ret = []
        while len(heap) > 1:
            interval1 = heapq.heappop(heap)
            interval2 = heapq.heappop(heap)
            if interval1[1] >= interval2[0]:
                # 영역이 겹치는 경우
                heapq.heappush(heap, [interval1[0], max(interval1[1], interval2[1])])
            else:
                # 영역이 겹치지 않는 경우
                ret.append(interval1)
                heapq.heappush(heap, interval2)
        if heap:
            ret.append(heapq.heappop(heap))
        return ret

# optimal
# Runtime: 96 ms, faster than 23.87%
# Memory Usage: 16.2 MB, less than 57.26%
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()        # [[1, 2], [3, 4], [2, 3], [5, 6]] -> [[1, 2], [2, 3], [3, 4], [5, 6]]
        last = intervals[0]     # [1, 2]
        unique = []
        for cur in intervals:
            if cur[0] <= last[1]:
                # overlap
                last[1] = max(last[1], cur[1])  # 1) last: [1, 2], cur: [2, 3] => last = [1, 3], unique = []
                                                # 2) last: [1, 3], cur: [3, 4] => last = [1, 4], unique = []
            else:
                # not overlap
                unique.append(last)             # 3) last: [1, 4], cur: [5, 6] => last=[5, 6], unique = [[1, 4]]
                last = cur
        unique.append(last)                     # 4) unique = [[1, 4], [5, 6]]
        return unique