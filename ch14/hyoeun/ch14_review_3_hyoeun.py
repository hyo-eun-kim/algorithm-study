# https://programmers.co.kr/learn/courses/30/lessons/49189
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

from collections import defaultdict, deque
import heapq

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
   
    distance = {}
    visited = []
    stack = []
    heapq.heappush(stack, (1, 1))
    while stack:
        dist, cur = heapq.heappop(stack)
        if cur not in distance:
            distance[cur] = dist
            for _next in graph[cur]:
                heapq.heappush(stack, (dist+1, _next))
    
    max_value = max(distance.values())
    return sum([True for i in distance.values() if i == max_value])
    