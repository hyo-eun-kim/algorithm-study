class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        일단 정렬하고 병합하기
        """
        intervals = sorted(intervals, key = lambda x: x[0]) # 정렬
        res = []

        for i in intervals:
            if res and i[0] <= res[-1][1]: # 겹치는 조건
                res[-1][1] = max(res[-1][1], i[1]) # res를 고쳐야 원하는 결과를 얻을 수 있음.

            else:
                res.append(i)

        return res
