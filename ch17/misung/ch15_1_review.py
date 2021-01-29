## 디스크 컨트롤러
# 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 
# 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. 
#(단, 소수점 이하의 수는 버립니다)

import heapq

def solution(jobs):
    n = len(jobs)
    time, end, heap = 0, -1, []  # 현재시간, 최근 끝난 시간
    cnt = 0 # 처리한 프로세스 수
    ans =0 

    while cnt < n :
        for s,t in jobs:  # 프로세스 입력시간, 끝날때까지 걸리는 시간
            if end < s <= time :  # 현재 작업이 시작되는 지점과 이전 작업이 끝나는 지점이 겹쳐지는 경우
                ans += (time-s)  # 현재시간 기준 프로세스가 얼마나 기다렸는지.
                heapq.heappush(heap, t)
            
        if len(heap) > 0:
            ans += len(heap) *heap[0] # 가장 빨리 끝나는 프로세스가 끝날때까지 heap 에 있는프로세스 전부 대기
            end = time # 끝난 시간
            time += heapq.heappop(heap) # 가장 빨리끝나는 프로세스가 걸리는 시간을 더해줌
            cnt +=1 # 프로세스가 끝났으니까 +1

        else:  # heap 에 아무것도 없으므로 시간을 +1 해줌
            time +=1

            
    return ans//n