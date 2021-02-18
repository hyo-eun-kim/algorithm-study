'''
71. 해밍 거리

두 정수를 입력받아 몇 비트가 다른지 계산하라.

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
       
화살표 표시한 두 군데 비트가 다르므로 정답은 2다.

'''

# 내 풀이
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
    # 28 ms