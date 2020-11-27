'''
leetcode 739 (**)
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

T = [73, 74, 75, 71, 69, 72, 76, 73]
your output should be [1, 1, 4, 2, 1, 1, 0, 0]
'''
from typing import List


# 책 풀이 아이디어 좋당 ..
def dailyTemperatures(T: List[int]) -> List[int]:
    ans = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            ans[last] = i-last  # 현재 index - stack 속 index
        stack.append(i)
    return ans


if __name__ == "__main__":
    T = [73, 74, 75, 71, 72, 69, 72, 76, 73]
    ans = dailyTemperatures(T)
    for x in ans:
        print(x, end=" ")