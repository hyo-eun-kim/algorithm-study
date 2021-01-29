'''
64. 원점에 K번째로 가까운 점

평면상에 points 목록이 있을 때, 원점 (0, 0)에서 K번 가까운 점 목록을 순서대로 출력하라. 평면상 두 점의 거리는 유클리드 거리로 한다.

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

(1，3) 과의 거리는 sqrt(10)이고, (-2 ， 2) 와의 거리는 sqrt(8)이다. 두 번째가 더 가까우며， K=1로
가장 가까운 거리 K개는 [[-2，2]] 이다.

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]

'''

# 내 풀이

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x:x[0]**2+x[1]**2)
        return points[:K]
    # 612 ms