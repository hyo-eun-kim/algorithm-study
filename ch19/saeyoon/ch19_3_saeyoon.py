"""
## 19-3. 두 정수의 합

두 정수 a와 b의 합을 구하라. + 또는 - 연산자는 사용할 수 없다.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & mask) if b > 0 else a


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(1, 2))
    print(sol.getSum(-2, 3))