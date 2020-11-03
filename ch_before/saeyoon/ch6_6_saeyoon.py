"""
## 6-6. 가장 긴 팰린드롬 부분 문자열

가장 긴 팰린드롬 부분 문자열을 출력하라
"""

import re
from collections import defaultdict


def solution(s):
    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    answer = ""
    for i in range(len(s) - 1):
        answer = max(answer, expand(i, i), expand(i, i + 1), key=len)
    return answer


if __name__ == '__main__':
    s1 = "babad"
    s2 = "cbbd"
    print(solution(s1))
    print(solution(s2))