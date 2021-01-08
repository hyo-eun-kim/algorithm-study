# k 경유지 내 가장 저렴한 항공권
# 시작점에서 도착점까지의 가장저렴한 가격을 계산하되,
# k개의 경유지 이내에 도착하는 가격을 리턴하라
# 경로가 존재하지 않을 경우 -1을 리턴한다.

# 주의할점 !? 경유지의 수가 한정되어있다는것!
import collections
def findCheapestPrice(self, n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    
    graph = collections.defaultdict(list)
    for u,v,w in flights:   # 출발, 도착, 거리(비용)
        graph[u].append((v,w))

    Q = [(0,src,K)]  # 가격, 정점, 남은 경유지수

    while Q:
        price, node,K = heapq.heappop(Q) 
        if node == dst : # 목적지에 도착했으면
            return price # 비용 리턴

        if K>=0 : # 경유지가 남았으면
            for v,w in graph[node] : # node와 인접한 곳 탐색
                alt = price+w
                heapq.heappush(Q,(alt,v,K-1))
            #print('Q',Q)

    return -1