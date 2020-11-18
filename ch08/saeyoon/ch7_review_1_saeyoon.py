"""
## 복습 7-1. 부분합

# 백준 1806
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

N (10 ≤ N < 100,000), S (0 < S ≤ 100,000,000)
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수
"""

# 부분합이 연속된 수라는 제한이 있으므로 투포인터 알고리즘을 통해 접근
n, s = map(int, input().split())
lst = list(map(int, input().split()))

left, right, temp_sum = 0, 0, lst[0]
length = n + 1

while left <= right and right < n:
    if temp_sum < s:
        right += 1
        if right == n:
            break
        temp_sum += lst[right]
    # 합이 s인 것 중 가장 짧은 것을 구하기 위해 짧은 length로 업데이트
    else:
        length = min(length, right - left + 1)
        temp_sum -= lst[left]
        left += 1

print(length if length != n + 1 else 0)