"""
## 복습 6-2. 수들의 합

# 백준 2003
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합
A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""


def solution() -> int:
    # 2 pointer algorithm
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    sum_a = 0
    start = 0
    end = 1
    tmp = a[start]

    while start < n:
        # 검색 완료
        if end == n and tmp < m:
            break

        # 원소 한 개의 합이 m인 경우
        if tmp == m:
            sum_a += 1
            tmp -= a[start]
            start += 1
        # 원소의 값이 m보다 작거나 같을 경우
        elif tmp < m:
            tmp += a[end]
            end += 1
        # 원소의 값이 m보다 클 때
        else:
            tmp -= a[start]
            start += 1

    return sum_a


if __name__ == '__main__':
    print(solution())