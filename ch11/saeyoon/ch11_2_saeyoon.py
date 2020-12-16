"""
## 11-2. 보석과 돌

J는 보석이며, S는 갖고 있는 돌이다.
S에는 보석이 몇 개나 있을까?
대소문자는 구분한다.
"""
from typing import *


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 28ms
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb")) # 3