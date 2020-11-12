# https://www.acmicpc.net/problem/2003

def solution():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            sum_val = sum(A[i:j+1])
            if sum_val == M:
                cnt += 1
            elif sum_val > M:
                break
    return cnt


def solution2():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))



if __name__ == "__main__":
    print(solution())