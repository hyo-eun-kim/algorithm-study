# https://www.acmicpc.net/problem/2559
# 백준 - 수열
# 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오. 

N,K = map(int, input().split())   # N = 전체 날짜수 , K = 합을 구하기 위한 연속적인 날짜의 수
tem = list(map(int,input().split())) # 매일 측정한 온도

sum_t = [0] * (N+1)
for i in range(1, N+1):
    sum_t[i] = tem[i-1] + sum_t[i-1]

ans=-100000000
for i in range(N-K+1):
    result_sum = sum_t[i+K] - sum_t[i]
    if ans< result_sum :
        ans =result_sum

print(ans)