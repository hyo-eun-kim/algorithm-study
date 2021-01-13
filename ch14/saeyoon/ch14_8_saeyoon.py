"""
## 14-8. 최소 높이 트리

노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.
"""
from typing import *
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 232ms
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        # 첫번째 리프노드 추가
        leaves = []
        for i in range(n + 1):
            # value의 개수가 1개인 경우는 리프노드
            if len(graph[i]) == 1:
                leaves.append(i)

        # 노드 개수에서 리프 노드 개수만큼 빼며 2개 이하가 남을 때까지 반복
        # 루트 노드가 1개 또는 2개일 수 있음
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            # 리프 노드에 대해 반복
            for leaf in leaves:
                # 리프 노드의 이웃 노드에서 리프 노드를 제거
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                # 리프 노드의 이웃 노드가 리프 노드인 경우 new_leaves에 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # 리프 노드 업데이트
            leaves = new_leaves

        return leaves


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, ], [5, 4]]))