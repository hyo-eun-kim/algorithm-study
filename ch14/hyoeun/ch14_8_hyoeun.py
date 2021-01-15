'''
49. 최소 높이 트리
노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록 반환하라
https://leetcode.com/problems/minimum-height-trees/
'''

from collections import defaultdict
from typing import List
from collections import defaultdict

# 풀이 생각이 신기하다 ...
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 말단에 위치한 node
        terminals = [i for i in graph if len(graph[i]) == 1]
        # 왜 n > 2?
        # 마지막에 남은 값이 홀수 개일 떄는 루트가 최송 1개가 되지만, 짝수 개일 때는 2개가 될 수 있다 -> 왜 이렇게 되는가?
        # 3인 경우에는 -> 1개로 줄어들 수 있고 / 4인 경우에는 -> 2개로 줄어들 수 있기 때문에! 와...!
        while n > 2:
            n -= len(terminals)
            new_terminals = []
            for node in terminals:
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                if len(graph[neighbor]) == 1:
                    new_terminals.append(neighbor)
            terminals = new_terminals
        return terminals
