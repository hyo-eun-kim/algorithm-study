"""
## 9-3. 일일 온도

매일의 화씨 온도 리스트 T를 입력받아서,
더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
"""
from typing import *


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 508 ms
        answer = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                answer[index] = i - index
            stack.append([i, t])

        return answer

    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        # 500 ms
        answer = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(sol.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))