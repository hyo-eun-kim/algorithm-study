class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list) # 값을 list로 지정
        for a,b in sorted(tickets): # 어휘 순으로 그래프 만듦
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0)) # 어휘 순으로 방문하기 위해 dequeue
            route.append(a)

        dfs('JFK')
        return route[::-1] # reverse해서 리턴해야 어휘 순으로 나옴
