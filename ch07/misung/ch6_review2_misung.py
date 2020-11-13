'''
백준 2003번
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

# for lo in range(N):
#     temp = 0
#     for hi in range(lo,N):
#         temp += A[hi]
#         if temp == M:
#             cnt +=1
#             break
#         elif temp>M:
#             break

# print(cnt)

#sumArr 첫항부터 자신 까지의 합이 담긴 리스트
sumArr = [0] * (N + 1)
for i in range(1, N + 1):
    sumArr[i] = sumArr[i-1] + A[i-1]  

for lo in range(N):
    temp = 0 
    for hi in range(lo+1,N+1):
        temp = sumArr[hi]-sumArr[lo]
        if temp == M:
            cnt +=1
            break
        elif temp>M:
            break
print(cnt)