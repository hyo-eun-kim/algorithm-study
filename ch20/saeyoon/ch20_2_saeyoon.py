"""
## 20-2. 부분 문자열이 포함된 최소 윈도우

문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 100ms
        need = Counter(t)
        missing = len(t)
        i = start = end = 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            # 모든 char가 존재할 때
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j - i <= end - start:
                    start, end = i, j
                need[s[i]] += 1
                i += 1
                missing += 1
        return s[start:end]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))
    print(sol.minWindow("a", "a"))