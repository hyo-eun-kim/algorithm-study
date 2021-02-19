# 프로그래머스 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
# n 	times	 return
# 6	   [7, 10]	 28

def solution(n, times):
    left , right = 1, max(times)*n # right = 최악의 경우 = 가장 비효율적인 심사관에서 다 받는경우
    answer = 0
    while left<=right :
        mid =(left+right)//2  # 한 심사관에게 주어진 시간
        people =0
        for i in times:
            people +=mid//i  # 각 심사관마다 주어진 시간동안 심사할수 있는 사람의 수
            
            if people>=n: # 모든 사람을 심사하면 반복문 끝
                answer =mid
                right = mid-1  # 모든 사람을 심사할수 있으면 시간을 줄여본다
                break
        

        
        if people<n: # 모든 사람을 심사할수 없는경우, 한 심사관에게 주어진 시간을 늘려본다.
            left = mid+1 
    return answer