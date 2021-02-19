"""
## 19-5. 1비트의 개수

부호없는 정수형을 입력받아 1비트의 개수를 출력하라.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(11))