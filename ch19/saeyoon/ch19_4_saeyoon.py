"""
## 19-4. UTF-8 검증

입력값이 UTF-8 문자열이 맞는지 검증하라.
"""
from typing import *


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0b0:
                start += 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.validUtf8([197, 130, 1]))
    print(sol.validUtf8([235, 140, 4]))