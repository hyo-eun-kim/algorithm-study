# 1비트의 개수
# 부호없는 정수형을 입력받아 1비트의 개수를 출력하라.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')