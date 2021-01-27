"""
## 17-5. 유효한 애너그램

t가 s의 애너그램인지 판별하라.
"""
from typing import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 48ms
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))