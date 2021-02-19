# 해밍거리
# 두 정수를 입력받아 몇 비트가 다른지 계산하라.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        