'''
부분합

10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
'''

# 내 풀이 
# 런타임 에러가 난다. 추후 해결 예정
N, S = map(int, input().split())
A = list(map(int, input().split()))
left = 0
right = 1
total = A[0]
cnt = N + 1

while left < right:
    if total >= S:
        cnt = min(cnt, right - left)
        total -= A[left]
        left += 1
        
        if total < S and right < N:
            total += A[right]
            right += 1
    else:
        if right >= n:
            break
        total += A[right]
        right += 1
        
        if right - left >= cnt:
            total -= A[left]
            left += 1
print(cnt)


# 답안 
N, S = map(int, input().split())
A = list(map(int, input().split()))
left, right, hap, result, temp = 0, 0, A[0], 0, 0
while left <= right and right < N:
    if hap < S:
        right += 1
        if right < N:
            hap += A[right]
    elif hap >= S:
        temp = right - left + 1
        if result == 0:
            result = temp
        else:
            result = min(result, temp)
        if left < right:
            hap -= A[left]
            left += 1
        else:
            right += 1
            if right < N:
                hap += A[right]
print(result)
# 188ms