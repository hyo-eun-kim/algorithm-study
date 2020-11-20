# 투 포인터 풀이
n,m = tuple(list(map(int, input().split(" "))))
num_arr = list(map(int, input().split(" ")))

"""
count = 0
start, end = 0, len(num_arr)

while start < end:
    tmp = sum(num_arr[start:end])
    if tmp > m:
        end -= 1
    elif tmp < m:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1


print(count)

점점 좁혀나가는 방식이 아니라 앞에서부터 넓혀나가는 방식으로 해야할 것 같음.
그리고 얘는 인덱스가 중요해서 sort 하면 안됨.
"""

"""
backstep을 안하고 무조건 한 방향으로만 움직임.
"""
count = 0
start = 0
sum = 0

for elem in num_arr:
    sum += elem # 시작부터 부분합 구함 (즉, end pointer가 증가하는 역할임)
    while sum >= m:
        if sum == m:
            count += 1
        sum -= num_arr[start] # 왼쪽 포인터 증가함
        start += 1 # 왼쪽 포인터 증가

print(count)
