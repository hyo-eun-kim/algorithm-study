"""
## 22-2. 괄호를 삽입하는 여러 가지 방법

숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.
"""
from typing import *


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            return [eval(str(l) + op + str(r)) for l in left for r in right]

        if input.isdigit():
            return [int(input)]

        results = []
        for idx, val in enumerate(input):
            if val in "+-*":
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                results.extend(compute(left, right, val))
        return results


if __name__ == '__main__':
    sol = Solution()
    print(sol.diffWaysToCompute("2*3-4*5"))