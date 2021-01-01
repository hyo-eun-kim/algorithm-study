# 코스 스케줄
# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
# 코스 개수 n과 이 쌍들을 입력으로 받았을때, 모든 코스가 완룐 가능한지 판별하라.

# 그래프가 순환구조 인지 판별하는 문제로 풀이할수 있다.
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
import collections

def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # 그래프 구성
    graph = collections.defaultdict(list)
    for a,b in prerequisites :
        graph[a].append(b)

    visited = set()  # 이미 방문한 노드들 저장

    def dfs(i):
        if i in visited : # 이미 방문한 노드면, 순환구조니까
            return False

        visited.add(i)  # 방문한 노드 추가

        for b in graph[i]:
            if not dfs(b):  
                return False

        visited.remove(i)  # 모든 탐색이 끝나면 방문기록 삭제! 
        return True

    for x in list(graph):
        if not dfs(x):  # DFS 가 True 가 아니면 False 
            return False

    return True    