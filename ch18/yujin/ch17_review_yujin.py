def solution(scoville, K):
    import heapq
    answer = 0
    if K == 0: # 예외 처리
        return 0

    # 힙 사용
    heapq.heapify(scoville)

    while True:
        new = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        heapq.heappush(scoville,new) # push
        answer += 1
        smallest = heapq.heappop(scoville)
        if smallest < K:
            if smallest == 0:
                return -1
            continue
        else:
            break


    return answer
