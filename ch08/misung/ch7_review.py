# 백준 1806 부분합
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

N, S = map(int, input().split())   # 10 15
A = list(map(int, input().split()))  # [5 1 3 5 10 7 4 9 2 8]
 

#먼저 0~n까지의 합을 구해줌
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
    
#투포인터 설정
answer = 100001  # 10,000 이하의 자연수로 이루어진 길이 N짜리 수열
start = 0
end = 1

#알고리즘 실행
while start != N:
    if sum_A[end] - sum_A[start] >= S: 
        if end - start< answer:  
            answer = end - start # S 이상이면 길이를 저장
        start += 1  # 다음으로 넘어가기
        
    else:
        if end != N: 
            end += 1
        else:
            start += 1

#답이 없을 경우 & 있을 경우
if answer != 100001: 
    print(answer)
else:
    print(0)
