'''
https://programmers.co.kr/learn/courses/30/lessons/43238
문제 설명
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

# 시간초과
import heapq
def solution(n, times):
    next_time = [(time, time) for time in times]
    heapq.heapify(next_time)

    for i in range(n - 1):
        total_time, unit_time = heapq.heappop(next_time)
        heapq.heappush(next_time, (total_time + unit_time, unit_time))

    return heapq.heappop(next_time)[0]


def solution(n, times):
    min_time = 1
    max_time = max(times)*n
    ans = 1
    while min_time <= max_time:
        mid = (min_time+max_time)//2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            ans = mid
            max_time = mid-1
        else:
            min_time = mid+1
    return ans