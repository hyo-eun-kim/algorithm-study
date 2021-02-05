# 프로그래머스 더 맵게 
# 

import heapq

def solution(scv, K): 
    answer = 0 
    h = [] 
    
    for i in scv: 
        heapq.heappush(h,i) 
    while h[0] < K: 
        try: 
            heapq.heappush(h,heapq.heappop(h)+(heapq.heappop(h)*2)) 
        except IndexError: 
            return -1 
        answer += 1 
    return answer
