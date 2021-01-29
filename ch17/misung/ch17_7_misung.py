# 원점에 k 번째로 가까운 점
# 평명상에 points 목록이 있을때, 원점 (0,0) 에서 k번 가까운
# 점 목록을 순서대로 출력하라
# 평면상 두 점의 거리는 유클리드 거리로한다.

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap =[]
        for (x,y) in points:
            dist = x**2 +y**2
            heapq.heappush(heap,(dist,x,y))
        
        result =[]
        for _ in range(K):
            (dist, x,y)= heapq.heappop(heap)
            result.append((x,y))
        return result