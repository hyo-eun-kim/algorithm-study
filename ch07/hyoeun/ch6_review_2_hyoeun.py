# https://www.acmicpc.net/problem/2003

# time exceeded
def solution():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    cnt = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            sum_val = sum(A[i:j+1])
            if sum_val == M:
                cnt += 1
                break
            elif sum_val > M:
                break
    return cnt


# submit code
def solution2():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    cnt = 0
    left_index, right_index = 0, 0 # 이 시작 지점 정하는 것만 하면 풀 수 있다 .. !
    while right_index <= len(A)-1:
        sum_val = sum(A[left_index:right_index+1])
        if sum_val == M:
            cnt += 1
            left_index += 1
            right_index += 1
        elif sum_val < M:
            right_index += 1
        else:
            # sum_val > M
            left_index += 1
    return cnt


if __name__ == "__main__":
    print(solution2())