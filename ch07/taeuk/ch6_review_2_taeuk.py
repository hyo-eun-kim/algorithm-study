'''
수들의 합 2

N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    left = right = Sum = cnt = 0
    while True:
        if Sum >= M:
            Sum -= A[left]
            left += 1
        elif right == N:
            break
        else:
            Sum += A[right]
            right += 1
        if Sum == M:
            cnt += 1
    return cnt

print(solve())

