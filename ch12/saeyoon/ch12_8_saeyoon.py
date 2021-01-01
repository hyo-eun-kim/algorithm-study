"""
## 12-8. 코스 스케줄

0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력을 받았을 때 모든 코스가 완료 가능한지 판별하라.
"""
from typing import *
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 100ms
        courses = defaultdict(set)
        pres = defaultdict(set)
        for course, pre in prerequisites:
            courses[course].add(pre) # 수강과목(key): 선수과목(value)
            pres[pre].add(course) # 선수과목(key): 수강과목(value)

        no_pre_courses = [i for i in range(numCourses) if not courses[i]]
        count = 0
        while no_pre_courses:
            # 선수과목이 없는 과목부터 수강
            no_pre = no_pre_courses.pop()
            count += 1
            # 선수과목으로 하는 과목들을 대상으로 수강 (해당 과목 제거)
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                # 선수 과목을 이미 모두 수강했으면 no_pre_courses에 추가
                if not courses[course]:
                    no_pre_courses.append(course)

        return count == numCourses


    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 92ms
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            # 이미 방문한 노드를 다시 방문하게 되면 순환 구조로 간주할 수 있음
            if visited[i] == -1:
                return False
            # 탐색이 끝났다면 1로 설정하고 다시 방문하지 않도록 함
            if visited[i] == 1:
                return True
            # 방문했음을 표시
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            # 모든 이웃노드를 방문 후 visited을 1로 설정
            visited[i] = 1
            return True

        # 각 노드 방문
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
    print(sol.canFinish(4, [[0, 1], [1, 2], [1, 3]]))