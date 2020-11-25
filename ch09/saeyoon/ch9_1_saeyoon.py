"""
## 9-1. 유효한 괄호

괄호로 된 입력값이 올바른지 판별하라
"""
from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        # 32 ms
        if s[0] in [")", "]", "}"]:
            return False

        stack = []
        for i in s:

            if stack and i == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and i == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

        return True if not stack else False

    def isValid2(self, s: str) -> bool:
        # 24 ms
        stack = []
        table = {')': '(',
                 ']': '[',
                 '}': '{'}

        for i in s:
            if i not in table:
                stack.append(i)
            elif not stack or table[i] != stack.pop():
                return False

        return True if not stack else False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()[]{}"))
    print(sol.isValid2("()[]{}"))
