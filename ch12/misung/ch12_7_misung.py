# 일정 재구성
# [from, to] 로 구성된 항공권 목록을 이용해 JFK 에서 출발하는 여행 일정을 구성하라.
# 여러 일정이 있는 경우 사전 어휘순으로 방문한다.

#Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
import collections

def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = collections.defaultdict(list)

    for a , b in sorted(tickets):  # 애초에 tickets 를 정렬하여도 된다!
        graph[a].append(b)

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))  # pop(0) 을 해야 첫번째꺼 pop! ,  JKF -> MUC -> LHR -> SFO -> SJC 
        route.append(a)  # 뒤에서부터 append 됨.

    route = []
    dfs('JFK')
    return route[::-1]
    