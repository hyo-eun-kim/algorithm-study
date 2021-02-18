"""
## 19-2. 해밍 거리

두 정수를 입력받아 몇 비트가 다른지 계산하라.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1, 4))