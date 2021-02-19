# 두 정수의 합
# 두 정수 a 와 b 의 합을 구하라.
# + 또는 -연산자는 사용할수 없다.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while(b & mask >0) :
            carry = (a&b) <<1
            a = a^b
            b = carry
        return (a & mask) if b > 0 else a
