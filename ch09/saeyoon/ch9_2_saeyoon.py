"""
## 9-2. 중복 문자 제거

중복된 문자를 제외하고 사전식 순서로 나열하라.
"""
from typing import *
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_index = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)

        return ''.join(stack)


    def removeDuplicateLetters2(self, s: str) -> str:
        counter = Counter(s)
        seen = set()
        stack = []

        for i in s:
            counter[i] -= 1
            if i in seen:
                continue
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(i)
            seen.add(i)

        return ''.join(stack)



if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters("bcabc"))
    print(sol.removeDuplicateLetters2("cbacdcbc"))