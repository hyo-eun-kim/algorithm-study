# 네트워크 딜레이 타임
# k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
#불가능할 경우 -1을 리턴한다.
# 입력값 (u,v,w) 는 각각 출발지, 도착지, 소요시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.
import collections

def networkDelayTime(times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    graph =collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u,v,w in times:    # 출발,도착,소요시간
        graph[u].append((v,w))   

    # 큐 선언
    Q = [(0,k)]  # (소요시간, 정점)  ==> 초기값은 0이고, k부터 시작됨
    dist = collections.defaultdict(int)  # 거리를 의미

    while Q :
        time, node = heapq.heappop(Q)  # 소요시간, 노드  (최솟값을 추출)
        if node not in dist :  # dist 에 노드 포함여부 체크 , dist에 존재하지 않으면, 
            dist[node] = time  # dist 값으로 
            for v,w in graph[node] :
                alt = time + w
                heapq.heappush(Q,(alt,v))  # Q 에 (시작점, 거리) push

    if len(dist) ==N :
        return max(dist.values())

    return -1