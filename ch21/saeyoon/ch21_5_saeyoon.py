"""
## 21-5. 쿠키 부여

아이들에게 1개씩 쿠키를 나눠줘야 한다.
각 아이 child_i 마다 그리드 팩터 (Greed Factor) g_i를 갖고 있으며，
이는 아이가 만족히는 최소 쿠키의 크기를 말한다.
각 쿠키 cookie_j는 크기 s_j갖고 있으며，s_j>=g_i 이어야 아이가 만족하며 쿠키를 받는다.
최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
"""
from typing import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 152ms
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i


if __name__ == '__main__':
    sol = Solution()
    print(sol.findContentChildren([1, 2, 3], [1, 1]))
    print(sol.findContentChildren([1, 2], [1, 2, 3]))