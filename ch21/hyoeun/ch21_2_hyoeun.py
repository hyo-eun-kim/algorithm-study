'''
406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/
여러 명의 사람들이 줄을 서 있다. 각각의 사람은 [h, k] 정수 쌍을 갖는데,
h은 사람의 키, k는 앞의 사람들 중 자신의 키 이상인 사람들의 수를 의미한다.
줄 서 있는 사람들의 순서대로 정렬해보아라.
'''
import heapq

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # max heap -> greedy algorithm에서 heap 사용빈도 높다
        # 내림차순 정렬
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        # 가장 큰 값 하나씩 꺼내면서 정렬
        result = []
        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1], [-p[0], p[1]])

        return result
