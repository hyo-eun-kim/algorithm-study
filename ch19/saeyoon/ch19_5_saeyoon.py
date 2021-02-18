"""
## 19-5. 1비트의 개수

입력값이 UTF-8 문자열이 맞는지 검증하라.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(11))