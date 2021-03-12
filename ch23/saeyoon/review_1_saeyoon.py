"""
## 섬 연결하기

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때
필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
예를 들어 A 섬과 B 섬 사이에 다리가 있고,
B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
"""

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    points = set([costs[0][0]])
    while len(points) < n:
        for i, cost in enumerate(costs):
            if cost[0] in points and cost[1] in points:
                continue
            if cost[0] in points or cost[1] in points:
                points.update([cost[0], cost[1]])
                answer += cost[2]
                costs.pop(i)
                break
    return answer