''''
https://www.acmicpc.net/problem/1806
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
'''

def solution():
    N, S = map(int, input().split())
    input_list = list(map(int, input().split()))

    min_length = len(input_list)+1  # 이거 때문에 ...
    left_ptr = 0
    right_ptr = 0

    x = input_list[0]
    while right_ptr < N:
        if x > S:
            min_length = min(min_length, right_ptr-left_ptr+1)
            x -= input_list[left_ptr]
            left_ptr += 1
        elif x == S:
            min_length = min(min_length, right_ptr-left_ptr+1)
            if right_ptr == N-1:
                break
            x += input_list[right_ptr + 1]
            right_ptr += 1
        else:
            # x < S
            if right_ptr == N-1:
                break
            x += input_list[right_ptr+1]
            right_ptr += 1

    if min_length == N+1:
        return 0
    return min_length


if __name__ == "__main__":
    print(solution())

