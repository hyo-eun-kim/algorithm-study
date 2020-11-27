'''
https://www.acmicpc.net/problem/2559
'''
import sys

# 104ms
def solution():
    N, K = map(int, input().split())
    array = list(map(int, input().split()))

    max_val = -sys.maxsize
    left, right = 0, K
    sum_val = sum(array[left:right])
    for i in range(N-K):
        max_val = sum_val if sum_val > max_val else max_val
        sum_val += (array[right]-array[left])
        left += 1
        right += 1
    max_val = sum_val if sum_val > max_val else max_val
    return max_val


if __name__ == "__main__":
    print(solution())