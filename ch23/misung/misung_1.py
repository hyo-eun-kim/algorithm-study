# 그리디 알고리즘
# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 
# 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 
# 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합(방문한 점들 저장)
    while len(routes)<n: # 방문한 점의 개수가 n보다 작을때 까지
        for i, cost in enumerate(costs):  # 추가하려는 선의 양끝 지점이 같은 집합에 속하지 않는지 확인
            if cost[0] in routes and cost[1] in routes:  # 이미 경로에 추가된경우
                continue
            if cost[0] in routes or cost[1] in routes: # 경로에 추가되지 않은경우
                routes.update([cost[0], cost[1]]) # 경로를 업데이트 한다! (값을 여러개 동시에 추가)
                ans += cost[2] # 비용을 더한다.
                costs[i] = [-1, -1, -1] 
                break
    return ans