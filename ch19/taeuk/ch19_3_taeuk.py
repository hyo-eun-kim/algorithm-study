'''
72. 두 정수의 합

두 정수 a와 b의 합을 구하라. + 또는 - 연산자는 사용할 수 없다.

'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        
        while (b & mask) > 0:

            carry = ( a & b ) << 1

            a = (a ^ b) # XOR 연산
            b = carry
        
        return (a & mask) if b > 0 else a
    # 28 ms 
    
# 납득이 잘 가지 않는다...