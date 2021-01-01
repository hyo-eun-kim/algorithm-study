'''
https://leetcode.com/problems/course-schedule/
'''
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for post, pre in prerequisites:
            graph[post].append(pre)

        traced = set()  # 이미 방문한 노드를 저장

        def dfs(i):
            if i in traced:
                # 이미 방문했던 노드를 재방문
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i) # 이해 X....
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True


# faster than 73% (96ms)
# less than 68% (15.6MB)
# 참고코드 : https://leetcode.com/problems/course-schedule/discuss/58750/Python-easy-to-understand-indegree-solution-with-comments.
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
        # 딕셔너리 사용하는 것보다 메모리 사용량 적다!
        indegree = [[] for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            # [i, j] : i 과목의 선수 과목이 j이다
            # i node의 indegree j: i <- j
            # i node의 outdegree j : i -> j
            # [수리통계2, 수리통계1] : 수리통계2 <- 수리통계1 이렇게 연결해주는 과정
            indegree[pre[0]].append(pre[1])  # key: 과목, value: 선수과목
            outdegree[pre[1]].append(pre[0])  # key: 선수과목, value: 과목

        # 선수과목이 없는 과목 리스트
        start = [i for i in range(numCourses) if not indegree[i]]
        count = 0
        while start:  # 선수과목이 없는 과목부터 시작
            new_start = []
            for i in start:
                count += 1
                for j in outdegree[i]:
                    # i과목을 선수과목으로 하는 과목 j
                    indegree[j].remove(i) # j과목 중 선수과목 i 제거
                    if not indegree[j]:
                        # 선수과목이 모두 충족될 수 있다면
                        new_start.append(j)
            start = new_start

        return count == numCourses


if __name__ == "__main__":
    solution = Solution2()
    print(solution.canFinish(2, [[1, 0]]))
    #print(solution.canFinish(5, [[1, 2], [2, 3], [3, 4], [3, 5]]))